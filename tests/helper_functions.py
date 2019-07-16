import json
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification


class HelperFunctions:
    @staticmethod
    def _load_json():
        """Loads a pipedesign json file for test purposes."""

        with open("data/json/0a234fea9682454facab730c0a7f83f0.json") as json_file:
            pipedesign_json = json.load(json_file)

        return pipedesign_json

    @staticmethod
    def _create_test_model():
        """Used to create a machine learning model for test purposes."""

        X, y = make_classification(
            n_samples=1000,
            n_features=4,
            n_informative=2,
            n_redundant=0,
            random_state=0,
            shuffle=False,
        )
        clf = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)
        clf.fit(X, y)

        return clf
