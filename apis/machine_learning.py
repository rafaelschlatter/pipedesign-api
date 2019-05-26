from flask import jsonify
from flask_restplus import Resource, Namespace, fields
from ml import model


api = Namespace('machinelearning', description='Namespace holding all methods related to machine learning.')

pipedesign_model = api.model(name="Pipedesign model", model=
    {
        "timestamp": fields.String(required=True),
        "design_id": fields.String(required=True),
        "pipe_segments": fields.List(cls_or_instance=fields.Raw, required=True),
        "viability": fields.Raw(required=True)
    }
)

@api.route("/")
class MachineLearning(Resource):
    def get(self):
        """Trains a model on pipedesign data from Azure blob storage."""

        return jsonify({"Error": "Not implemented yet"})


    @api.expect(pipedesign_model, validate=True)
    def post(self):
        """Returns a prediction on the viability of a single pipedesign."""

        data = api.payload
        predictor = model.Model()
        prediction = predictor.predict(data)
        return jsonify({"prediction": prediction, "confidence": "Not implemented yet"})
