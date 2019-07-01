from flask import Flask
from flask_restplus import Api

from .apis.prediction import api as ns1
from .apis.ml_model import api as ns2
from .apis.pipedesign import api as ns3


api = Api(
    version='0.1',
    title='Pipedesign ML Api',
    description='An API to retrieve predictions about the constructability of pipe systems. Maintainer: rafaelschlatter@gmail.com.',
    contact="rafaelschlatter@gmail.com"
)

api.add_namespace(ns1)
api.add_namespace(ns2)
api.add_namespace(ns3)


def create_app():
    app = Flask(__name__)
    api.init_app(app)

    return app
