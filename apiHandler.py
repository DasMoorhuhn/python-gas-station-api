'''
Diese lib holt sich die Informationen von Tankstellen via API https://tankerkoening.de und gibt diese als Objekte zurück
Projektseite GitLab: https://gitlab.com/HendrikHeine/python-gas-station-api/
Hendrik Heine, 2022
'''


import pgeocode
import requests as _requests
from secretHandler import secret as _secret
from classes import *

class api:
    def __init__(self, postalCode:int, secret:_secret) -> None:
        '''postalCode: Die Postleitzahl\nsecret: Das secret Objekt'''
        __geo = pgeocode.Nominatim(country="de") # Dies ist ein fester Wert, da die API nur für Deutschland funktioniert
        location = __geo.query_postal_code(codes=postalCode)

        self.__city = city(lat=location["latitude"], lng=location["longitude"], name=location["place_name"], postalCode=location["postal_code"], communityCode=location["community_code"])
        self.__apiKey = secret.getApiKey()
        self.__baseURL = "https://creativecommons.tankerkoenig.de/json"
        self.__priceURL = f"{self.__baseURL}/prices.php" #Preisabfrage
        self.__listURL = f"{self.__baseURL}/list.php" # Umkreissuche
        self.__detailURL = f"{self.__baseURL}/detail.php" # Details zu einer bestimmten Tankstelle
        self.__reportURL = f"{self.__baseURL}/complaint.php" # Zum Melden von falschen Angaben
        self.version = "0.0.1"
        self.date = "09.05.2022"

        self.__stations = [] 

    def __sortStationList(self, stationList:list, sortedBy:str):
        listForReturn = []
        try:
            if sortedBy == "price":
                pass
            if sortedBy == "postCode":
                pass
            if sortedBy == "distance":
                pass
            if sortedBy == "none":
                listForReturn = stationList

        finally:
            return listForReturn


    def getGasStations(self, raduisInKM:float=10.0, spritType:str="all", onlyInThisPostCode:bool=False, sortedBy:str="none"):
        '''Max Radius: 25KM\nSpritTypes: e5, e10, diesel, all\nOnlyInThisPostCode: Zeigt nur Tanketsllen mit der passenden Postleitzahl\nSortedBy: price, postCode, distance, none'''
        req = f"{self.__listURL}?lat={self.__city.lat}&lng={self.__city.lng}&rad={raduisInKM}&sort=dist&type={spritType}&apikey={self.__apiKey}"
        response = _requests.api.get(req).json()
        if response["ok"] and response["status"] == "ok":
            for station in response["stations"]:
                self.__stations.append(gasSation(value=station))
        listForReturn = []
        for station in self.__stations:
            station:gasSation
            if onlyInThisPostCode:
                if station.postCode == self.__city.postalCode:
                    listForReturn.append(station)
            else:
                listForReturn.append(station)

        return self.__sortStationList(stationList=listForReturn, sortedBy=sortedBy)

    def getGasStaionDetails(self, staionID:str):
        '''Mehr details zu einer bestimmten Tankstelle'''
        req = f"{self.__detailURL}?id={staionID}&apikey={self.__apiKey}"
        response = _requests.api.get(req).json()
        if response["ok"] and response["status"] == "ok":
            return gasSationDetail(response["station"])
        else:
            return 1