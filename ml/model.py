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


    def validate_json(self, json_data):
        """Validates the json coming with the request. Should be used before attempting to make a prediction.

        Args:
            json_data (dict): Input data to make a prediction.

        Returns: True if json format is correct, false if json is missing parameters.
        """

        if not isinstance(json_data, dict):
            return False

        req_params = ["timestamp", "design_id", "pipe_segments", "viability"]
        for param in req_params:
            if param in json_data:
                continue
            else:
                return False

        return True


    def persist_model(self, trained_model):
        """Saves a model to a storage place (Azure storage blob?).
        """
        pass
