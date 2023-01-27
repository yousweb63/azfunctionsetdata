import pandas as pd
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import json
import datetime
class GetBlob():
    def formatFileName():
            today = datetime.datetime.now()
            day = today.day
            month = today.month
            year = today.year
            filename = f"{year}/{month}/{day}/report_st_clerm_2023-01-27.json"
            return filename
    def getFileFromBlobStorage(filename):
            container_name="storms"
            constr = "DefaultEndpointsProtocol=https;AccountName=youssstorageacount;AccountKey=O4Spd1j3ykpimoKh0iWJLYgShpbUakEnAjlqp3TJ5p0HSp3Nc+Okl0F0Q3dbg5s9H/JoMupHs4VX+AStTx5H7A==;BlobEndpoint=https://youssstorageacount.blob.core.windows.net/;"
            blob_service_client = BlobServiceClient.from_connection_string(constr)
            container_client = blob_service_client.get_container_client(container_name)
            blob_client = container_client.get_blob_client(filename)
            streamdownloader = blob_client.download_blob()
            fileReader = json.loads(streamdownloader.readall())
            return fileReader
    def jsonToDataframe(fileReader):
            df = pd.read_json(json.dumps(fileReader), orient='records')
            return df