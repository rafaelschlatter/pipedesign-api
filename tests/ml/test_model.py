import os
import pytest
import numpy as np
from datetime import datetime
from src.ml import preprocessor, model


class TestModel():
    def test_train(self):
        proc = preprocessor.Preprocessor()
        pipedesigns = proc.download_blobs(os.environ["CONTAINER_NAME_DATA"], number_of_blobs=40)
        dataset = proc.create_training_data(pipedesigns)
        clf = model.Model()
        clf.train(training_data=dataset)
        assert clf.classifier
        assert str(type(clf.classifier)) == "<class 'sklearn.ensemble.forest.RandomForestClassifier'>"
        assert str(type(clf.last_train_time_utc)) == "<class 'datetime.datetime'>"


    def test_predict(self):
        proc = preprocessor.Preprocessor()
        pipedesigns = proc.download_blobs(os.environ["CONTAINER_NAME_DATA"], number_of_blobs=40)
        dataset = proc.create_training_data(pipedesigns)
        clf = model.Model()
        clf.train(training_data=dataset)

        test_data = proc.azure_blob_to_json(container_name=os.environ["CONTAINER_NAME_DATA"], blob_name="test_blob_do_not_delete")
        label, confidence = clf.predict(json_data=test_data)
        # TODO: This depends on the currently trained model, think of a fix here.
        assert (label[0] == 0 or label[0] == 1)
        assert (confidence[0][0] <= 1 and confidence[0][0] >= 0)
