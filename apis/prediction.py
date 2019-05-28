import os
from flask import jsonify
from flask_restplus import Resource, Namespace, fields
from ml import model
from ml import preprocessor
from apis.cache import cache


api = Namespace('prediction', description='Namespace holding all methods related to predictions.')

pipedesign_model = api.model(name="Pipedesign model", model=
    {
        "timestamp": fields.String(required=True),
        "design_id": fields.String(required=True),
        "pipe_segments": fields.List(cls_or_instance=fields.Raw, required=True),
        "viability": fields.Raw(required=True)
    }
)


@api.route("/")
class Prediction(Resource):
    @api.expect(pipedesign_model, validate=True)
    def post(self):
        """Returns a prediction on the viability of a single pipedesign."""

        if "trained_model" not in cache.keys():
            return jsonify(
                {
                    "Error": "Model has not been trained yet. Train model first."
                }
            )

        label, confidence = cache["trained_model"].predict(api.payload)
        if label[0] == 1:
            prediction = "Viable"
        if label[0] == 0:
            prediction = "Unviable"

        return jsonify(
            {
                "label": "{}".format(label[0]),
                "prediction": "{}".format(prediction),
                "confidence": "{}".format(confidence[0][0])
            }
        )
        