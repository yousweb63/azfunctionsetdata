import datetime
import logging
from .getDataFromBlobStorage import GetBlob
from .setDataToSQL import SaveDataToSQL
import azure.functions as func

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()
    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
    filename = GetBlob.formatFileName()
    fileReader = GetBlob.getFileFromBlobStorage(filename)
    df = GetBlob.jsonToDataframe(fileReader)
    cnxn = SaveDataToSQL.connectToDb()
    SaveDataToSQL.insertData(cnxn,df)

        
