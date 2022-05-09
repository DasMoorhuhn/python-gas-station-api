import requests as _requests
from secretHandler import secret as _secret
import pgeocode

class city:
    def __init__(self, lat, lng, name, postalCode, communityCode) -> None:
        self.lat = lat
        self.lng = lng
        self.name = name
        self.postalCode = postalCode
        self.communityCode = communityCode

class api:
    def __init__(self, postalCode:int, secret:_secret) -> None:
        '''postalCode: Die Postleitzahl\nsecret: Das secret Objekt'''
        __geo = pgeocode.Nominatim(country="de")
        location = __geo.query_postal_code(codes=postalCode)

        self.__city = city(lat=location["latitude"], lng=location["longitude"], name=location["place_name"], postalCode=location["postal_code"], communityCode=location["community_code"])
        
        self.__apiKey = secret.getApiKey()
        self.__baseURL = "https://creativecommons.tankerkoenig.de/json"
        self.__priceURL = f"{self.__baseURL}/prices.php" #Preisabfrage
        self.__listURL = f"{self.__baseURL}/list.php" # Umkreissuche
        self.__detailURL = f"{self.__baseURL}/detail.php" # Details zu einer bestimmten Tankstelle

        

    def getLatAndLong(self):
        print(self.__city.name)

    def getGasStations(self):
        pass