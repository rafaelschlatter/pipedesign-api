import os
import pytest
import numpy as np
from src.ml import preprocessor, model


class TestModel():
    def test_train(self):
        proc = preprocessor.Preprocessor()
        pipedesigns = proc.download_blobs(os.environ["CONTAINER_NAME_DATA"], number_of_blobs=10)
        dataset = proc.create_training_data(pipedesigns)
        clf = model.Model()
        clf.train(training_data=dataset)
        assert clf.classifier
        assert str(type(clf.classifier)) == "<class 'sklearn.ensemble.forest.RandomForestClassifier'>"


    def test_predict(self):
        proc = preprocessor.Preprocessor()
        pipedesigns = proc.download_blobs(os.environ["CONTAINER_NAME_DATA"], number_of_blobs=10)
        dataset = proc.create_training_data(pipedesigns)
        clf = model.Model()
        clf.train(training_data=dataset)

        test_data = proc.azure_blob_to_json(container_name=os.environ["CONTAINER_NAME_DATA"], blob_name="test_blob_do_not_delete")
        label, confidence = clf.predict(json_data=test_data)
        assert label[0] == 0
        assert confidence[0][0] == 1.0
