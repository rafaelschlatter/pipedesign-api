from flask import jsonify
from flask_restplus import Resource
from ml_api.server import server
from ml_api.models.pipedesign_model import pipedesign_model
from ml_api.ml import model


ns_ml = server.api.namespace('machinelearning', description='Namespace holding all methods related to machine learning.')


@ns_ml.route("/")
class MachineLearning(Resource):
    def get(self):
        """Trains a model on pipedesign data from Azure blob storage."""

        return jsonify({"Error": "Not implemented yet"})


    @server.api.expect(pipedesign_model, validate=True)
    def post(self):
        """Returns a prediction on the viability of a single pipedesign."""

        data = server.api.payload
        predictor = model.Model()
        prediction = predictor.predict(data)
        return jsonify({"prediction": prediction, "confidence": "Not implemented yet"})
