import os
from datetime import datetime
from sklearn.ensemble import RandomForestClassifier
from src.ml import preprocessor, model
from src.infrastructure import blobhandler


class TestModel:
    def test_train(self):
        handler = blobhandler.BlobHandler()
        pipedesigns = handler.download_blobs(
            os.environ["CONTAINER_NAME_DATA"], number_of_blobs=50
        )
        proc = preprocessor.Preprocessor()
        dataset = proc.create_training_data(pipedesigns)
        clf = model.Model()
        clf.train(training_data=dataset)
        assert clf.classifier
        assert isinstance(clf.classifier, RandomForestClassifier)
        assert isinstance(clf.last_train_time_utc, datetime)

    def test_predict(self):
        handler = blobhandler.BlobHandler()
        pipedesigns = handler.download_blobs(
            os.environ["CONTAINER_NAME_DATA"], number_of_blobs=50
        )
        proc = preprocessor.Preprocessor()
        dataset = proc.create_training_data(pipedesigns)
        clf = model.Model()
        clf.train(training_data=dataset)

        test_data = handler.azure_blob_to_json(
            container_name=os.environ["CONTAINER_NAME_DATA"],
            blob_name="test_blob_do_not_delete",
        )[1]
        label, confidence = clf.predict(json_data=test_data)
        # TODO: This depends on the currently trained model, think of a fix here.
        assert label[0] == 0 or label[0] == 1
        assert confidence[0][0] <= 1 and confidence[0][0] >= 0
