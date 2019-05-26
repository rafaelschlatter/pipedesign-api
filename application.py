from flask import Flask, request, jsonify
from flask_restplus import Resource, Api, fields
from ml import model


app = Flask(__name__)
api = Api(
    app=app,
    version='0.1',
    title='Pipedesign ML Api',
    description='An API to retrieve predictions about the constructability of pipe systems.',
    contact="rafaelschlatter@gmail.com"
)

ns_ml = api.namespace('machinelearning', description='Namespace holding all methods related to machine learning.')
ns_model = api.namespace('model', description="Namespace holding all methods related to the model.")
ns_pipedesign = api.namespace('pipedesign', description="Namespace holding all methods related to pipedesigns.")

pipedesign_model = api.model(name="Pipedesign model", model=
    {
        "timestamp": fields.String(required=True),
        "design_id": fields.String(required=True),
        "pipe_segments": fields.List(cls_or_instance=fields.Raw, required=True),
        "viability": fields.Raw(required=True)
    }
)


@ns_ml.route("/")
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


@ns_model.route("/")
class Model(Resource):
    def get(self):
        """Gets the current model information."""

        return jsonify({"Error": "Not implemented yet"})


    def post(self):
        """Updates the model (new parameters, training schedule, etc...)."""

        return jsonify({"Error": "Not implemented yet"})


@ns_pipedesign.route("/<pipedesign_id>")
@api.param('pipedesign_id', 'Alphanumeric id of pipedesign')
class Pipedesign(Resource):
    def get(self, pipedesign_id):
        """Gets a pipedesign in json format."""

        return jsonify({"Error": "Not implemented yet"})


    @api.expect(pipedesign_model, validate=True)
    def post(self):
        """Stores a pipedesign in to Azure blob storage."""

        return jsonify({"Error": "Not implemented yet"})


if __name__ == '__main__':
    app.run(debug=True)
