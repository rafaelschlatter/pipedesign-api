import os
import pytest
import numpy as np
from ml import preprocessor, model


class TestModel():
    def test_train(self):
        proc = preprocessor.Preprocessor()
        pipedesigns = proc.download_blobs(os.environ["CONTAINER_NAME_DATA"])
        dataset = proc.create_training_data(pipedesigns)
        clf = model.Model()
        clf.train(training_data=dataset)
        assert clf.classifier
        assert str(type(clf.classifier)) == "<class 'sklearn.ensemble.forest.RandomForestClassifier'>"


    def test_predict(self):
        proc = preprocessor.Preprocessor()
        pipedesigns = proc.download_blobs(os.environ["CONTAINER_NAME_DATA"])
        dataset = proc.create_training_data(pipedesigns)
        clf = model.Model()
        clf.train(training_data=dataset)

        test_data = proc.azure_blob_to_json(container_name=os.environ["CONTAINER_NAME_DATA"], blob_name="test_blob_do_not_delete")
        label, confidence = clf.predict(json_data=test_data)
        assert str(type(label[0])) == "<class 'numpy.int32'>"
        assert label[0] == 0
        assert str(type(confidence[0][0])) == "<class 'numpy.float64'>"
        assert confidence[0][0] == 1.0