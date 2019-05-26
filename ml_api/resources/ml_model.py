from flask import jsonify
from flask_restplus import Resource
from ml_api.server import server


ns_model = server.api.namespace('model', description="Namespace holding all methods related to the model.")

@ns_model.route("/")
class Model(Resource):
    def get(self):
        """Gets the current model information."""

        return jsonify({"Error": "Not implemented yet"})


    def post(self):
        """Updates the model (new parameters, training schedule, etc...)."""

        return jsonify({"Error": "Not implemented yet"})