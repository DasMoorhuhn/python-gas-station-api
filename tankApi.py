import apiHandler
import secretHandler as sh
from classes import *

secret = sh.secret()
value = secret.loadFromSecret()
if value == 0:
    api = apiHandler.api(postalCode=26127, secret=secret)
    stations = api.getGasStations(onlyInThisPostCode=True, raduisInKM=5, spritType="all")
    for station in stations:
        station:gasSation
        stationDetail = api.getGasStaionDetails(staionID=station.id)
        stationDetail:gasSationDetail
        print(station.brand)
        print(stationDetail.wholeDay)
        print("")
else:
    exit("Error reading secret")