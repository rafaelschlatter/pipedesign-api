import os
import json
from azure.storage.blob import BlockBlobService, PublicAccess


class BlobHandler():
    """This class communicates with Azure blob storage."""

    def __init__(self):
        """Constructor."""

        self.block_blob_service = BlockBlobService(account_name=os.environ["STORAGE_ACC_NAME"], account_key=os.environ["BLOB_KEY1"])
        self.container_name = os.environ["CONTAINER_NAME_DATA"]
    

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


    def json_to_azure_blob(self, container_name, pipedesign_json):
        """Saves a pipedesign in json format to Azure blob.

        Args:
            container_name (string): The container to store the json file in.
            pipedesign_json (dict): The pipedesign in json format.

        Returns (bool): True if saving to blob was successful, False otherwise.
        """
        pipedesign_string = json.dumps(pipedesign_json)
        try:
            self.block_blob_service.create_blob_from_text(container_name=container_name, blob_name=pipedesign_json["design_id"], text=pipedesign_string)
            return True
        except Exception as e:
            return e
        