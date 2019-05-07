from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "I love you Dawn, and gratulerer til nye kontrakten! Greetings, Rafael :)"