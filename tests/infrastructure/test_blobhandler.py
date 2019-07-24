import os
from sklearn.naive_bayes import GaussianNB
from azure.common import AzureMissingResourceHttpError, AzureHttpError
from src.infrastructure import blobhandler
from tests.helper_functions import HelperFunctions


class TestBlobHandler:
    def test_download_blobs(self):
        handler = blobhandler.BlobHandler()
        blobs = handler.download_blobs(
            container_name=os.environ["CONTAINER_NAME_DATA"], number_of_blobs=5
        )
        assert len(blobs) == 5

    def test_azure_blob_to_json_success(self):
        handler = blobhandler.BlobHandler()
        result = handler.azure_blob_to_json(
            container_name=os.environ["CONTAINER_NAME_DATA"],
            blob_name="test_blob_do_not_delete",
        )
        assert result[0] == True
        json_data = result[1]
        assert isinstance(result[1], dict)
        assert "timestamp" in json_data.keys()
        assert "design_id" in json_data.keys()
        assert "pipe_segments" in json_data.keys()
        assert "viability" in json_data.keys()

    def test_azure_blob_to_json_failure(self):
        handler = blobhandler.BlobHandler()
        result = handler.azure_blob_to_json(
            container_name=os.environ["CONTAINER_NAME_DATA"],
            blob_name="non_existant_blob_name",
        )
        assert result[0] == False

    def test_json_to_azure_blob_success(self):
        handler = blobhandler.BlobHandler()
        pipedesign_json = HelperFunctions._load_json()
        result = handler.json_to_azure_blob(
            container_name=os.environ["CONTAINER_NAME_DATA"],
            pipedesign_json=pipedesign_json,
        )
        assert result[0] == True

    def test_json_to_azure_blob_failure(self):
        handler = blobhandler.BlobHandler()
        pipedesign_json = HelperFunctions._load_json()
        result = handler.json_to_azure_blob(
            container_name="invalid_container_name", pipedesign_json=pipedesign_json
        )
        assert result[0] == False
        assert isinstance(result[1], AzureHttpError)

    def test_azure_blob_to_model_success(self):
        handler = blobhandler.BlobHandler()
        result = handler.azure_blob_to_model(
            model_id="test_model_1_do_not_delete",
            container_name=os.environ["CONTAINER_NAME_MODELS"],
        )
        assert result[0] == True
        assert isinstance(result[1], GaussianNB)

    def test_azure_blob_to_model_failure(self):
        handler = blobhandler.BlobHandler()
        result = handler.azure_blob_to_model(
            model_id="non_existant_model_id",
            container_name=os.environ["CONTAINER_NAME_MODELS"],
        )
        assert result[0] == False
        assert isinstance(result[1], AzureMissingResourceHttpError)

    def test_model_to_azure_blob_success(self):
        model = HelperFunctions._create_test_model()
        handler = blobhandler.BlobHandler()
        result = handler.model_to_azure_blob(
            model=model,
            container_name=os.environ["CONTAINER_NAME_MODELS"],
            blob_name="test_model_2_do_not_delete",
        )
        assert result[0] == True

    def test_model_to_azure_blob_failure(self):
        model = HelperFunctions._create_test_model()
        handler = blobhandler.BlobHandler()
        result = handler.model_to_azure_blob(
            model=model, container_name="non_existant_container"
        )
        assert result[0] == False
        assert isinstance(result[1], AzureHttpError)

    def test_training_metrics_to_azure_blob_success(self):
        metrics_dict = HelperFunctions._create_training_metrics()
        handler = blobhandler.BlobHandler()
        result = handler.training_metrics_to_azure_blob(
            training_metrics_dict=metrics_dict,
            container_name=os.environ["CONTAINER_NAME_MODELS"]
        )
        assert result[0] == True

    def test_training_metrics_to_azure_blob_failure(self):
        metrics_dict = HelperFunctions._create_training_metrics()
        handler = blobhandler.BlobHandler()
        result = handler.training_metrics_to_azure_blob(
            training_metrics_dict=metrics_dict,
            container_name="non_existant_container"
        )
        assert result[0] == False
        assert isinstance(result[1], AzureHttpError)
