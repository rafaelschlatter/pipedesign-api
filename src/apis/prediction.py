from flask import jsonify
from flask_restplus import Resource, Namespace
from flask_restplus import abort
from src.ml import preprocessor
from src.ml.features import pipe_features
from src.apis.cache import cache
from src.apis.pipedesign import pipedesign_model


api = Namespace('prediction', description='Namespace holding all methods related to predictions.')


@api.route("/predict_current/")
class Prediction(Resource):
    @api.expect(pipedesign_model, validate=True)
    def post(self):
        """Returns a prediction on the viability of a single pipedesign using the current trained model."""

        if "trained_model" not in cache.keys():
            message = "Model has not been trained yet. Train model first."
            abort(405, custom=message)

        label, confidence = cache["trained_model"].predict(api.payload)
        if label[0] == 1:
            prediction = "Viable"
        if label[0] == 0:
            prediction = "Unviable"

        return jsonify(
            {
                "pipedesign_id": "{}".format(api.payload["design_id"]),
                "label": "{}".format(label[0]),
                "prediction": "{}".format(prediction),
                "confidence": "{}".format(confidence[0][0])
            }
        )


@api.route("/predict_pickled/")
class PickledPrediction(Resource):
    @api.expect(pipedesign_model, validate=True)
    def post(self):
        """Returns a prediction on the viability of a single pipedesign using the activated pickled model."""
        
        if "pickled_model" not in cache.keys():
            message = "No pickled model is activated yet. Activate model first."
            abort(405, custom=message)

        proc = preprocessor.Preprocessor()
        pipedesign_sample = proc.flatten_pipesegments(api.payload)
        label = cache["pickled_model"].predict(pipedesign_sample[pipe_features])
        confidence = cache["pickled_model"].predict_proba(pipedesign_sample[pipe_features])

        if label[0] == 1:
            prediction = "Viable"
        if label[0] == 0:
            prediction = "Unviable"

        return jsonify(
            {
                "pipedesign_id": "{}".format(api.payload["design_id"]),
                "label": "{}".format(label[0]),
                "prediction": "{}".format(prediction),
                "confidence": "{}".format(confidence[0][0])
            }
        )
