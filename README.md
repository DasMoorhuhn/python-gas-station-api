# Python Tankstellen Api Wrapper 
Dies ist ein API Wrapper für Tankstellen in Deutschland. Als Quelle wird [TankerKönig](https://tankerkoenig.de/) verwendet. Ziel ist es, einfache Objekte zu bekommen mit allen Daten einer Tankstelle. Jaaaa ich weiß, es gibt die [PyTankerKoening](https://pypi.org/project/pytankerkoenig/) Lib, die haut aber das JSON einfach so raus. 

## Getting started
1. API Key: </br>
    1. [API Key anlegen](https://creativecommons.tankerkoenig.de/) -> API-KEY </br>
    2. Neue Datei mit dem Namen `secret.txt` im Ordner der lib erstellen </br>
    3. Den API Key in die Datei kopieren. </br> </br>
2. SercretHandler: </br>
    1. Das Objekt secret vom secretHandler erstellen </br>
    2. Die Methode `loadFromSecret` ausführen. Damit wird die Datei `secret.txt` ausgelesen.
    3. Rückgabewerte: </br>
        - 0: Secret wurde geladen </br>
        - 1: Fehler beim Lesen von `secret.txt` </br> </br>
3. ApiHandler:
    1. api Objekt erstellen. Mit übergeben wird die Postleitzahl und das secret Objekt
    2. Methoden:
        - ## getGasStations(raduisInKM:float, spritType:str, onlyInThisPostCode:bool, sortedBy:str):
          - raduisInKM: 
            - max: 25
            - Radius in Kilometer um die Postleitzahl herum
          - spritType:
            - e5
            - e10
            - diesel
            - all
          - onlyInThisPostCode:
            - True: Gibt nur die Tankstellen zurück, die mit der Postleitzahl vom api Objekt (classes.city) übereinstimmen
            - False: Gibt alle Tankstellen im diffinierten Radius zurück
          - sortedBy [TODO]:
            - price: Sortiert die Liste nach Preis (Von Günstig nacg Teuer)
            - postCode: Sortiert die Liste nach Postleitzahl (Aufsteigend)
            - distance: Sortiert die Liste nach Distanz zur Postleitzahl (Aufsteigend, KM)
            - none: gibt die Liste ohne überarbeitung weiter
          - return value:
            - Liste der Tankstellen
        - ## getGasStationDetail(stationID:str):
          - stationID: die Tankstellen ID
          - return value:
            - gasStationDetail Objekt (classes.gasStationDetail)
            - 1 bei einem Fehler
    
## Libs
[pgeocode](https://pypi.org/project/pgeocode/): Für die Längen- und Breitengrade von einer Postleitzahl </br>
[requests](https://pypi.org/project/requests/): Zum aufrufen der TankerKönig API