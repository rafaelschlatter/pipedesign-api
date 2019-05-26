from flask import jsonify
from flask_restplus import Resource, Namespace, fields


api = Namespace('model', description="Namespace holding all methods related to the model.")

ml_model_model = api.model(name="Machine learning model", model=
    {
        "Name": fields.String(required=True),
        "model_type": fields.String(required=True),
        "last_trained": fields.String(required=True),
        "test_accuracy": fields.String(required=True)
    }
)


@api.route("/")
class Model(Resource):
    def get(self):
        """Gets the current model information."""

        return jsonify({"Error": "Not implemented yet"})


    def post(self):
        """Updates the model (new parameters, training schedule, etc...)."""

        return jsonify({"Error": "Not implemented yet"})