from flask import Flask, request, jsonify
from ml import model
app = Flask(__name__)


@app.route("/")
def hello():
    message = "Python flask website hosted on Azure Linux app service for free! \
        Test continous deployment (works only with public git repo)"
    return message


@app.route("/pipedesignml/api/predict", methods=['POST'])
def predict():
    data = request.get_json(force=True)

    predictor = model.Model()
    isValidJson = predictor.validate_json(data)
    if isValidJson == False:
        return jsonify({"Json format error": "Missing parameter"})

    prediction = predictor.predict(data)
    return jsonify({"prediction": prediction})


if __name__ == '__main__':
    app.run(debug=True)
