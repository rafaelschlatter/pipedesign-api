import os
from flask import jsonify
from flask_restplus import Resource, Namespace, fields
from src.ml import model
from src.ml import preprocessor
from src.apis.cache import cache
from src.apis.pipedesign import pipedesign_model


api = Namespace('prediction', description='Namespace holding all methods related to predictions.')


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
        