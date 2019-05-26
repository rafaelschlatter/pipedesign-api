from flask import jsonify
from flask_restplus import Resource, Namespace, fields


api = Namespace('pipedesign', description="Namespace holding all methods related to pipedesigns.")

pipedesign_model = api.model(name="Pipedesign model", model=
    {
        "timestamp": fields.String(required=True),
        "design_id": fields.String(required=True),
        "pipe_segments": fields.List(cls_or_instance=fields.Raw, required=True),
        "viability": fields.Raw(required=True)
    }
)


@api.route("/<pipedesign_id>")
@api.param('pipedesign_id', 'Alphanumeric id of pipedesign')
class Pipedesign(Resource):
    def get(self, pipedesign_id):
        """Gets a pipedesign in json format."""

        return jsonify({"Error": "Not implemented yet"})


    @api.expect(pipedesign_model, validate=True)
    def post(self):
        """Stores a pipedesign in to Azure blob storage."""

        return jsonify({"Error": "Not implemented yet"})