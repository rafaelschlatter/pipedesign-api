from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Python flask website hosted on Azure Linux app service for free!"
