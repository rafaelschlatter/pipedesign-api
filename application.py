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

ns_predict = api.namespace('predict', description='Namespace holding all methods related to predicting.')
ns_train = api.namespace('train', description='Namespace holding all methods related to training.')
ns_model = api.namespace('model', description="Namespace holding all methods related to the model.")

pipedesign_model = api.model(name="Pipedesign model", model=
    {
        "timestamp": fields.String(required=True),
        "design_id": fields.String(required=True),
        "pipe_segments": fields.List(cls_or_instance=fields.Raw, required=True),
        "viability": fields.Raw(required=True)
    }
)


@ns_predict.route("/")
class Prediction(Resource):
    @api.expect(pipedesign_model, validate=True)
    def post(self):
        """Returns a prediction on the viability of a single pipedesign."""

        data = api.payload
        predictor = model.Model()
        prediction = predictor.predict(data)
        return jsonify({"prediction": prediction, "confidence": "Not implemented yet"})


    @api.expect(pipedesign_model, validate=True)
    def post(self):
        """Returns predictions on the viability of a multiple pipedesigns."""

        return jsonify({"Error": "Not implemented yet"})


@ns_train.route("/")
class Training(Resource):
    def get(self):
        """Trains a model on pipedesign data from Azure blob storage."""

        return jsonify({"Error": "Not implemented yet"})


@ns_model.route("/")
class Model(Resource):
    def get(self):
        """Gets the current model information."""

        return jsonify({"Error": "Not implemented yet"})

if __name__ == '__main__':
    app.run(debug=True)
