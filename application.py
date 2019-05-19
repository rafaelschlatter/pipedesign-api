from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route("/")
def hello():
    message = "Python flask website hosted on Azure Linux app service for free! \
        Test continous deployment (works only with public git repo)"
    return message


@app.route("/pipedesignml/api/predict", methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = data["number"] * 2
    return jsonify({"prediction": prediction})


if __name__ == '__main__':
    app.run(debug=True)
