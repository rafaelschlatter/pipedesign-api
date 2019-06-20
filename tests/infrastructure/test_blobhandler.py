import os
from sklearn.naive_bayes import GaussianNB
from azure.common import AzureMissingResourceHttpError, AzureHttpError
from src.infrastructure import blobhandler
from tests.helper_functions import HelperFunctions


class TestBlobHandler():
    def test_azure_blob_to_json_success(self):
        handler = blobhandler.BlobHandler()
        json = handler.azure_blob_to_json(container_name=os.environ["CONTAINER_NAME_DATA"], blob_name="test_blob_do_not_delete")
        assert isinstance(json, dict)
        assert "timestamp" in json.keys()
        assert "design_id" in json.keys()
        assert "pipe_segments" in json.keys()
        assert "viability" in json.keys()


    def test_azure_blob_to_json_failure(self):
        handler = blobhandler.BlobHandler()
        json = handler.azure_blob_to_json(container_name=os.environ["CONTAINER_NAME_DATA"], blob_name="non_existant_blob_name")
        assert json == None


    def test_json_to_azure_blob_success(self):
        handler = blobhandler.BlobHandler()
        pipedesign_json = HelperFunctions._load_json()
        is_success = handler.json_to_azure_blob(container_name=os.environ["CONTAINER_NAME_DATA"], pipedesign_json=pipedesign_json)
        assert is_success == True

    
    def test_json_to_azure_blob_failure(self):
        handler = blobhandler.BlobHandler()
        pipedesign_json = HelperFunctions._load_json()
        is_success = handler.json_to_azure_blob(container_name="invalid_container_name", pipedesign_json=pipedesign_json)
        assert isinstance(is_success, AzureHttpError)


    def test_download_blobs(self):
        handler = blobhandler.BlobHandler()
        blobs = handler.download_blobs(container_name=os.environ["CONTAINER_NAME_DATA"], number_of_blobs=5)
        assert len(blobs) == 5


    def test_azure_blob_to_model_success(self):
        handler = blobhandler.BlobHandler()
        model = handler.azure_blob_to_model(model_id="test_model_1_do_not_delete",
            container_name=os.environ["CONTAINER_NAME_MODELS"])
        assert model[0] == True
        assert isinstance(model[1], GaussianNB)


    def test_azure_blob_to_model_failure(self):
        handler = blobhandler.BlobHandler()
        model = handler.azure_blob_to_model(model_id="non_existant_model_id",
            container_name=os.environ["CONTAINER_NAME_MODELS"])
        assert model[0] == False
        assert isinstance(model[1], AzureMissingResourceHttpError)


    def test_model_to_azure_blob_success(self):
        model = HelperFunctions._create_test_model()
        handler = blobhandler.BlobHandler()
        is_success = handler.model_to_azure_blob(model=model, container_name=os.environ["CONTAINER_NAME_MODELS"],
            blob_name="test_model_2_do_not_delete")
        assert is_success == True


    def test_model_to_azure_blob_failure(self):
        model = HelperFunctions._create_test_model()
        handler = blobhandler.BlobHandler()
        is_success = handler.model_to_azure_blob(model=model, container_name="non_existant_container")
        assert isinstance(is_success, AzureHttpError)
