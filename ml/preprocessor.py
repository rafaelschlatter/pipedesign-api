import os
import json
from azure.storage.blob import BlockBlobService, PublicAccess
import pandas as pd


class Preprocessor():
    """This class is used to download and preprocess pipedesign data in json format. It contains methods to do
    all transformations needed to create a dataset ready to be consumed by a machine learning model.
    """

    def __init__(self):
        """Constructor."""
        self.block_blob_service = BlockBlobService(account_name=os.environ["STORAGE_ACC_NAME"], account_key=os.environ["BLOB_KEY1"])
        self.container_name = os.environ["CONTAINER_NAME_DATA"]


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



    def download_blobs(self, container_name, number_of_blobs=5):
        """This method downloads json data from an Azure storage account (blobs).

        Args:
            container_name (string): The name of the container from which to retrieve blobs.
            number_of_blobs (int): Amount of blobs to load (retrieves most recent blobs).

        Returns (list): A list of dictionaries, one dict per pipedesign or None if all downloads failed.
        """

        # list_blobs() returns a generator of blobs, but the blobs do not contain the actual blob content.
        # list_blobs is only used to get the names of blobs, which then can be retrieved with 
        blob_generator = self.block_blob_service.list_blobs(container_name=container_name, num_results=number_of_blobs)

        pipedesign_list = []
        for blob in blob_generator:
            pipedesign_dict = self.azure_blob_to_json(container_name=container_name, blob_name=blob.name)
            if pipedesign_dict is not None:
                pipedesign_list.append(pipedesign_dict)
            else:
                continue

        if len(pipedesign_list) > 0:
            return pipedesign_list
        else:
            return None


    def azure_blob_to_json(self, container_name, blob_name):
        """Downloads a blob from an Azure storage account and transfers the content to json.

        Args:
            container_name (string): The container holding the blob.
            blob_name (string): The blob to load.

        Returns (dict): A json dict with the contents of the blob, or None if the download fails.
        """

        try:
            pipedesign_txt = self.block_blob_service.get_blob_to_text(container_name=container_name, blob_name=blob_name)
            return json.loads(pipedesign_txt.content)
        except Exception as e:
            print(e)
            return None
        