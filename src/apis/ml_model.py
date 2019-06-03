import os
import traceback
from flask import jsonify
from flask_restplus import Resource, Namespace, fields
from src.apis.cache import cache
from src.ml import model
from src.ml import preprocessor


api = Namespace('model', description="Namespace holding all methods related to the model.")

ml_model_model = api.model(name="Machine learning model", model=
    {
        "name": fields.String(required=True),
        "model_type": fields.String(required=True),
        "last_trained": fields.String(required=True),
        "test_accuracy": fields.String(required=True),
        "isinuse": fields.Boolean(required=True)
    }
)


@api.route("/")
class Model(Resource):
    def get(self):
        """Returns information about the current trained model."""

        if "trained_model" not in cache.keys():
            return jsonify(
                {
                    "Error": "Model has not been trained yet. Train model first."
                }
            )

        if cache["trained_model"]:
            return jsonify(
                {
                    "model_type": str(type(cache["trained_model"].classifier)),
                    "last_trained": str(cache["trained_model"].last_train_time_utc)
                }
            )


    def put(self):
        """Initiates and trains a random forest model that can be used to make predictions."""

        p = preprocessor.Preprocessor()
        num_blobs = 200
        try:
            blobs = p.download_blobs(os.environ["CONTAINER_NAME_DATA"], number_of_blobs=num_blobs)
        except Exception:
            return jsonify(
                {
                    "Error": "Failed to connect to azure blob.",
                    "Exception": str(traceback.format_exc())
                }
            )

        training_data = p.create_training_data(blobs)
        classifier = model.Model()
        classifier.train(training_data=training_data)
        cache["trained_model"] = classifier

        return jsonify({
            "training_result": "Success",
            "samples_used": "{}".format(num_blobs)
            }
        )
