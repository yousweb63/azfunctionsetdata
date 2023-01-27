import pyodbc

class SaveDataToSQL():
    def connectToDb():
            # Some other example server values are
            # server = '*****.windows.net' # for a named instance
            # server = 'myserver,port' # to specify an alternate port
            server = 'emilfrysql.database.windows.net' 
            database = 'auvstorms' 
            username = 'emilfryadminsql' 
            password = '641979Ab+'  
            cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)
            return cnxn

    def insertData(cnxn,df):
        while True:
            try:
                cursor = cnxn.cursor()
                for index, row in df.iterrows():
                    cursor.execute (
                            f"INSERT INTO dbo.reports ([dates], [localTime], [Temperature], [GroundTemperature], [DewPoint], [relativesHumidity], [Visibility], [Cloudiness], [windSpeedMean], [Direction], [GustsOfWind], [SeaPression], [variationPression], [Precipitation], [CumulusType], [CumulonimbusType],[FreezingLevelAltitude]) VALUES ('{row['date']}','{row['time']}',{row['Temperature']},{row['GroundTemperature']},{row['DewPoint']},{row['relativesHumidity']},'{row['Visibility']}',{row['Cloudiness']},{row['windSpeedMean']},{row['Direction']},{row['GustsOfWind']},{row['SeaPression']},{row['variationPression']},'{row['Precipitation']}',{row['CumulusType']},{row['CumulonimbusType']},{row['FreezingLevelAltitude']})"
                    )
                cnxn.commit()
                cursor.close()
                return 200
            except ValueError:
                return 500