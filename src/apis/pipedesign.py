import os
from flask import jsonify
from flask_restplus import Resource, Namespace, fields
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
    def get(self, pipedesign_id):
        """Returns a pipedesign in json format."""

        handler = blobhandler.BlobHandler()
        json = handler.azure_blob_to_json(container_name=os.environ["CONTAINER_NAME_DATA"], blob_name=pipedesign_id)

        if json == None:
            return jsonify({"Error": "The pipedesign with the given id does not exist in Azure blob."})
        else:
            return jsonify(json)


    @api.expect(pipedesign_model, validate=True)
    def post(self, pipedesign_id):
        """Stores a pipedesign as a json file to Azure blob storage."""

        pipedesign_json = api.payload
        handler = blobhandler.BlobHandler()
        # This overwrites the blob if it already exists.
        is_success = handler.json_to_azure_blob(container_name=os.environ["CONTAINER_NAME_DATA"], pipedesign_json=pipedesign_json)

        if is_success == True:
            return jsonify(
                {
                    "message": "Pipedesign saved successfully",
                    "containername": str(os.environ["CONTAINER_NAME_DATA"]),
                    "blobname": "{}".format(pipedesign_json["design_id"])
                }
            )

        else:
            return jsonify({"Error": "{}".format(str(is_success))})
