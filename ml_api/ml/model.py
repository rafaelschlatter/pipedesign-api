class Model():
    """This class holds a machine learning model which is exposed in the flask app.
    Client applications can request predictions from this model.
    """

    def train(self, training_data):
        """Trains a model on the given data.

        Returns: A trained model (e.g from scikit-learn).
        """
        pass


    def predict(self, json_data):
        """Returns a prediction for a single case, given the input data. Atm: Returns the number of pipesegments in the json file.

        Args:
            json_data (dictionary): Input data to make a prediction.
        """
        return len(json_data["pipe_segments"])


    def persist_model(self, trained_model):
        """Saves a model to a storage place (Azure storage blob?).
        """
        pass
