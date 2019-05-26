from flask import Flask
from flask_restplus import Api, Resource, fields


class Server(object):
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(
            self.app, 
            version='0.1',
            title='Pipedesign ML Api',
            description='An API to retrieve predictions about the constructability of pipe systems.',
            contact="rafaelschlatter@gmail.com"
        )

server = Server()