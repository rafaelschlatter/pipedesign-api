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

        prediction = cache["trained_model"].predict(api.payload)
        if prediction[0] == 1:
            verbal_pred = "Viable"
        if prediction[0] == 0:
            verbal_pred = "Unviable"
        return jsonify({"prediction": verbal_pred, "confidence": "Not implemented yet"})


    def get(self):
        """Trains a random forest model."""

        p = preprocessor.Preprocessor()
        num_blobs = 10
        blobs = p.download_blobs(os.environ["CONTAINER_NAME_DATA"], number_of_blobs=num_blobs)
        training_data = p.create_training_data(blobs)
        classifier = model.Model()
        classifier.train(training_data=training_data)
        cache["trained_model"] = classifier

        return jsonify({
            "training_result": "Success",
            "samples_used": "{}".format(num_blobs)
            }
        )
        