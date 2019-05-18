from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    message = "Python flask website hosted on Azure Linux app service for free! \
        Test continous deployment (works only with public git repo)"
    return message


if __name__ == '__main__':
    app.run(debug=True)
