import os
import json
import pandas as pd


class Preprocessor():
    """This class is used to download and preprocess pipedesign data in json format. It contains methods to do
    all transformations needed to create a dataset ready to be consumed by a machine learning model.
    """

    def __init__(self):
        """Constructor."""
        pass


    def create_training_data(self, pipedesign_list):
        """Creates a training dataset from a list of pipedesign dictionaries.

        Args:
            pipedesign_list (list): A list of pipedesign dictionaries.

        Returns: A pandas df or numpy array (to be decided...)
        """

        dataset = pd.DataFrame()
        for pipedesign in pipedesign_list:
            row = self.flatten_pipesegments(pipedesign)
            dataset = dataset.append(row)

        return dataset


    def flatten_pipesegments(self, pipedesign):
        """Flattens the pipesegments dict from a pipedesign.
        
        Args:
            pipedesign_json (dict):

        Returns: A normalized pandas df containing one pipedesign.
        """

        pipedesign_json = pd.io.json.json_normalize(pipedesign)
        for segment in pipedesign_json["pipe_segments"][0]:
            for point in segment["points"]:
                col_name_x = "segment_{0}_X_{1}".format(segment["segment_id"], point["end"])
                col_name_y = "segment_{0}_Y_{1}".format(segment["segment_id"], point["end"])
                col_name_z = "segment_{0}_Z_{1}".format(segment["segment_id"], point["end"])
                pipedesign_json[col_name_x] = point["X"]
                pipedesign_json[col_name_y] = point["Y"]
                pipedesign_json[col_name_z] = point["Z"]

        pipedesign_json.drop('pipe_segments', axis=1, inplace=True)
        return pipedesign_json
