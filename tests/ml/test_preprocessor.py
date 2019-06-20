import os
import pandas as pd
from src.infrastructure import blobhandler
from src.ml import preprocessor


class TestPreprocessor():
    def test_create_training_data(self):
        handler = blobhandler.BlobHandler()
        pipedesigns = handler.download_blobs(os.environ["CONTAINER_NAME_DATA"])
        proc = preprocessor.Preprocessor()
        dataset = proc.create_training_data(pipedesigns)
        assert isinstance(dataset, pd.DataFrame)


    def test_flatten_pipesegments(self):
        handler = blobhandler.BlobHandler()
        json = handler.azure_blob_to_json(container_name=os.environ["CONTAINER_NAME_DATA"], blob_name="test_blob_do_not_delete")[1]
        proc = preprocessor.Preprocessor()
        pipedesign_sample = proc.flatten_pipesegments(json)
        assert isinstance(pipedesign_sample, pd.DataFrame)
        assert pipedesign_sample.shape[0] == 1
        assert pipedesign_sample.shape[1] == 59
