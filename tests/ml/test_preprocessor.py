import os
import json
import pytest
import pandas as pd
from ml import preprocessor


class TestPreprocessor():
    def test_create_training_data(self):
        proc = preprocessor.Preprocessor()
        pipedesigns = proc.download_blobs(os.environ["CONTAINER_NAME_DATA"])
        dataset = proc.create_training_data(pipedesigns)
        assert type(dataset) == pd.DataFrame


    def test_azure_blob_to_json(self):
        proc = preprocessor.Preprocessor()
        json = proc.azure_blob_to_json(container_name=os.environ["CONTAINER_NAME_DATA"], blob_name="test_blob_do_not_delete")
        assert type(json) == dict
        assert "timestamp" in json.keys()
        assert "design_id" in json.keys()
        assert "pipe_segments" in json.keys()
        assert "viability" in json.keys()


    def test_json_to_azure_blob_success(self):
        proc = preprocessor.Preprocessor()
        pipedesign_json = self._helper_load_json()
        is_success = proc.json_to_azure_blob(container_name=os.environ["CONTAINER_NAME_DATA"], pipedesign_json=pipedesign_json)
        assert is_success == True

    
    def test_json_to_azure_blob_failure(self):
        proc = preprocessor.Preprocessor()
        pipedesign_json = self._helper_load_json()
        is_success = proc.json_to_azure_blob(container_name="invalid_container_name", pipedesign_json=pipedesign_json)
        assert str(type(is_success)) == "<class 'azure.common.AzureHttpError'>"


    def test_flatten_pipesegments(self):
        proc = preprocessor.Preprocessor()
        json = proc.azure_blob_to_json(container_name=os.environ["CONTAINER_NAME_DATA"], blob_name="test_blob_do_not_delete")
        df = proc.flatten_pipesegments(json)
        assert type(df) == pd.DataFrame
        assert df.shape[0] == 1
        assert df.shape[1] == 59


    def test_download_blobs(self):
        proc = preprocessor.Preprocessor()
        blobs = proc.download_blobs(container_name=os.environ["CONTAINER_NAME_DATA"], number_of_blobs=5)
        assert len(blobs) == 5


    def _helper_load_json(self):
        with open("data/json/0a234fea9682454facab730c0a7f83f0.json") as json_file:
            pipedesign_json = json.load(json_file)
        return pipedesign_json
