from flask import jsonify
from flask_restplus import Resource
from ml_api.server import server
from ml_api.models.pipedesign_model import pipedesign_model


ns_pipedesign = server.api.namespace('pipedesign', description="Namespace holding all methods related to pipedesigns.")

@ns_pipedesign.route("/<pipedesign_id>")
@server.api.param('pipedesign_id', 'Alphanumeric id of pipedesign')
class Pipedesign(Resource):
    def get(self, pipedesign_id):
        """Gets a pipedesign in json format."""

        return jsonify({"Error": "Not implemented yet"})


    @server.api.expect(pipedesign_model, validate=True)
    def post(self):
        """Stores a pipedesign in to Azure blob storage."""

        return jsonify({"Error": "Not implemented yet"})