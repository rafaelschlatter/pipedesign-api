from flask import jsonify
from flask_restplus import Resource, Namespace, fields
from apis.cache import cache


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


# Make this an Azure SQL database!
ml_models_db = [
    {
        "Name": "Random forest",
        "model_type": "",
        "last_trained": "never",
        "test_accuracy": "NaN",
        "isinuse": True
    }
]


@api.route("/")
class Model(Resource):
    def get(self):
        """Gets the current model information."""

        if cache["trained_model"]:
            here = "Yes"
        return jsonify({"latest_model": here})


    def post(self):
        """Updates the model (new parameters, training schedule, etc...)."""

        return jsonify({"Error": "Not implemented yet"})