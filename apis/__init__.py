from flask_restplus import Api

from .prediction import api as ns1
from .ml_model import api as ns2
from .pipedesign import api as ns3

api = Api(
    version='0.1',
    title='Pipedesign ML Api',
    description='An API to retrieve predictions about the constructability of pipe systems. Maintainer: rafaelschlatter@gmail.com.',
    contact="rafaelschlatter@gmail.com"
)

api.add_namespace(ns1)
api.add_namespace(ns2)
api.add_namespace(ns3)