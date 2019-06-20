import os
from flask import jsonify
from flask_restplus import Resource, Namespace, fields
from flask_restplus import abort
from src.infrastructure import blobhandler


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
    @api.response(200, 'Success', pipedesign_model)
    @api.response(404, "Not found")
    def get(self, pipedesign_id):
        """Returns a pipedesign in json format."""

        handler = blobhandler.BlobHandler()
        result = handler.azure_blob_to_json(container_name=os.environ["CONTAINER_NAME_DATA"], blob_name=pipedesign_id)

        if result[0] == False:
            message = "The pipedesign with the given id does not exist in Azure blob."
            abort(404, custom=message)
        else:
            return jsonify(result[1])


    @api.expect(pipedesign_model, validate=True)
    @api.response(200, 'Success')
    @api.response(503, "Service unavailable")
    def post(self, pipedesign_id):
        """Stores a pipedesign as a json file to Azure blob storage."""

        pipedesign_json = api.payload
        handler = blobhandler.BlobHandler()
        result = handler.json_to_azure_blob(container_name=os.environ["CONTAINER_NAME_DATA"], pipedesign_json=pipedesign_json)

        if result[0] == False:
            message = str(result[1])
            abort(503, custom=message)
        else:
            return jsonify(
                {
                    "message": "Pipedesign saved successfully",
                    "containername": str(os.environ["CONTAINER_NAME_DATA"]),
                    "blobname": "{}".format(pipedesign_json["design_id"])
                }
            )
