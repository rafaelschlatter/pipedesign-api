import os
import json
import pytest
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
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
        handler = blobhandler.BlobHandler()
        json = handler.azure_blob_to_json(container_name=os.environ["CONTAINER_NAME_DATA"], blob_name="non_existant_blob_name")
        assert json == None


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


    @pytest.mark.skip(reason="Fails on travis CI, works locally.")
    def test_azure_blob_to_model_success(self):
        handler = blobhandler.BlobHandler()
        model = handler.azure_blob_to_model(model_id="test_model_1_do_not_delete",
            container_name=os.environ["CONTAINER_NAME_MODELS"])
        assert str(type(model[1])) == "<class 'sklearn.ensemble.forest.RandomForestClassifier'>"
        assert model[0] == True


    def test_azure_blob_to_model_failure(self):
        handler = blobhandler.BlobHandler()
        model = handler.azure_blob_to_model(model_id="non_existant_model_id",
            container_name=os.environ["CONTAINER_NAME_MODELS"])
        assert str(type(model[1])) == "<class 'azure.common.AzureMissingResourceHttpError'>"
        assert model[0] == False
        

    def test_model_to_azure_blob_success(self):
        model = self._helper_create_test_model()
        handler = blobhandler.BlobHandler()
        is_success = handler.model_to_azure_blob(model=model, container_name=os.environ["CONTAINER_NAME_MODELS"],
            blob_name="test_model_2_do_not_delete")
        assert is_success == True


    def test_model_to_azure_blob_failure(self):
        model = self._helper_create_test_model()
        handler = blobhandler.BlobHandler()
        is_success = handler.model_to_azure_blob(model=model, container_name="non_existant_container")
        assert str(type(is_success)) == "<class 'azure.common.AzureHttpError'>"


    def _helper_load_json(self):
        with open("data/json/0a234fea9682454facab730c0a7f83f0.json") as json_file:
            pipedesign_json = json.load(json_file)
        return pipedesign_json


    def _helper_create_test_model(self):
        """Used to create a machine learning model for test purposes."""
        X, y = make_classification(n_samples=1000, n_features=4,
            n_informative=2,n_redundant=0,
            random_state=0, shuffle=False)
        clf = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)
        clf.fit(X, y)
        return clf
