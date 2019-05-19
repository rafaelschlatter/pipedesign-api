class Model():
    """This class holds a machine learning model which is exposed in the flask app.
    Client applications can request predictions from this model.
    """

    def predict(self, data):
        """Returns a prediction for a single case, given the input data.

        Args:
            data (dictionary): Input data to make a prediction.
        """
        return data["number"] * 2
