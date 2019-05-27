import os
from ml import preprocessor
import pandas as pd
from sklearn.ensemble import RandomForestClassifier


class Model():
    """This class holds a machine learning model which is exposed in the flask app.
    Client applications can request predictions from this model.
    """

    def __init__(self):
        """Constructor. Initiates a model object an trains a model."""
        proc = preprocessor.Preprocessor()
        blobs = proc.download_blobs(os.environ["CONTAINER_NAME_DATA"], number_of_blobs=10)
        training_data = proc.create_training_data(blobs)
        self.features = training_data.columns[5: ]
        self.trained_model = self.train(training_data)
    

    def train(self, training_data):
        """Trains a model on the given data.

        Args:
            training_data (pandas df): A dataframe containing training data for pipedesigns (namely geometry coordinates).

        Returns: A trained model (e.g from scikit-learn).
        """

        y = pd.factorize(training_data["viability.viable"])[0]
        clf = RandomForestClassifier(n_jobs=2, random_state=0)
        clf.fit(training_data[self.features], y)
        return clf


    def predict(self, json_data):
        """Returns a prediction for a single case, given the input data.

        Args:
            json_data (dictionary): Input data to make a prediction.
        """

        proc = preprocessor.Preprocessor()
        test_data_df = proc.flatten_pipesegments(json_data)
        return self.trained_model.predict(test_data_df[self.features])
