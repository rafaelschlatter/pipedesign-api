import os
import json
import pytest
from src.infrastructure import blobhandler


class TestBlobHandler():
    def test_azure_blob_to_json_success(self):
        handler = blobhandler.BlobHandler()
        json = handler.azure_blob_to_json(container_name=os.environ["CONTAINER_NAME_DATA"], blob_name="test_blob_do_not_delete")
        assert type(json) == dict
        assert "timestamp" in json.keys()
        assert "design_id" in json.keys()
        assert "pipe_segments" in json.keys()
        assert "viability" in json.keys()


    def test_azure_blob_to_json_failure(self):
        pass


    def test_json_to_azure_blob_success(self):
        handler = blobhandler.BlobHandler()
        pipedesign_json = self._helper_load_json()
        is_success = handler.json_to_azure_blob(container_name=os.environ["CONTAINER_NAME_DATA"], pipedesign_json=pipedesign_json)
        assert is_success == True

    
    def test_json_to_azure_blob_failure(self):
        handler = blobhandler.BlobHandler()
        pipedesign_json = self._helper_load_json()
        is_success = handler.json_to_azure_blob(container_name="invalid_container_name", pipedesign_json=pipedesign_json)
        assert str(type(is_success)) == "<class 'azure.common.AzureHttpError'>"

    
    def test_download_blobs(self):
        handler = blobhandler.BlobHandler()
        blobs = handler.download_blobs(container_name=os.environ["CONTAINER_NAME_DATA"], number_of_blobs=5)
        assert len(blobs) == 5


    def test_azure_blob_to_model_success(self):
        pass


    def test_azure_blob_to_model_failure(self):
        pass


    def test_model_to_azure_blob_success(self):
        pass


    def test_model_to_azure_blob_failure(self):
        pass


    def _helper_load_json(self):
        with open("data/json/0a234fea9682454facab730c0a7f83f0.json") as json_file:
            pipedesign_json = json.load(json_file)
        return pipedesign_json
