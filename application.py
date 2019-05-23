from flask import Flask, request, jsonify
from flask_restplus import Resource, Api, fields
from ml import model


app = Flask(__name__)
api = Api(app=app, version='0.1', title='Pipedesign ML Api', description='An API to retrieve predictions about the constructability of pipe systems.')


pipedesign_model = api.model(name="Pipedesign model", model=
    {
        "timestamp": fields.String(required=True),
        "design_id": fields.String(required=True),
        "pipe_segments": fields.Raw(required=False),
        "viability": fields.Raw(required=False)
    }
)


@api.route("/ml/predict", methods=["post"])
class Prediction(Resource):
    @api.expect(pipedesign_model)
    def post(self):
        """This method returns a prediction on the viability of a pipedesign.
        """

        data = api.payload
        predictor = model.Model()
        isValidJson = predictor.validate_json(data)
        if isValidJson == False:
            return jsonify({"Json format error": "Missing parameter"})

        prediction = predictor.predict(data)
        return jsonify({"prediction": prediction})


if __name__ == '__main__':
    app.run(debug=True)
