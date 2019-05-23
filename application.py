from flask import Flask, request, jsonify
from flask_restplus import Resource, Api, fields
from ml import model


app = Flask(__name__)
api = Api(app=app, version='0.1', title='Pipedesign ML Api', description='An API to retrieve predictions about the constructability of pipe systems.')

ns_machinelearning = api.namespace('machinelearning', description='Namespace holding all methods related to machine learning.')

pipedesign_model = api.model(name="Pipedesign model", model=
    {
        "timestamp": fields.String(required=True),
        "design_id": fields.String(required=True),
        "pipe_segments": fields.List(cls_or_instance=fields.Raw, required=True),
        "viability": fields.Raw(required=True)
    }
)


@ns_machinelearning.route("/")
class Prediction(Resource):
    @api.expect(pipedesign_model, validate=True)
    def post(self):
        """This method returns a prediction on the viability of a single pipedesign."""

        data = api.payload
        predictor = model.Model()
        prediction = predictor.predict(data)
        return jsonify({"prediction": prediction})


    def get(self):
        """Trains a model on pipedesign data from Azure blob storage."""

        return jsonify({"Error": "Not implemented yet."})


if __name__ == '__main__':
    app.run(debug=True)
