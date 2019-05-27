import os
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
