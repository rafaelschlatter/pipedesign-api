import pytest
import pandas as pd
from ml import preprocessor


class TestPreprocessor():
    def test_create_training_data(self):
        proc = preprocessor.Preprocessor()
        pipedesigns = proc.download_blobs("trainingdata")
        dataset = proc.create_training_data(pipedesigns)
        assert type(dataset) == pd.DataFrame


    def test_azure_blob_to_json(self):
        proc = preprocessor.Preprocessor()
        json = proc.azure_blob_to_json(container_name="trainingdata", blob_name="test_blob_do_not_delete")
        assert type(json) == dict
        assert "timestamp" in json.keys()
        assert "design_id" in json.keys()
        assert "pipe_segments" in json.keys()
        assert "viability" in json.keys()


    def test_download_blobs(self):
        proc = preprocessor.Preprocessor()
        blobs = proc.download_blobs(container_name="trainingdata", number_of_blobs=5)
        assert len(blobs) == 5
