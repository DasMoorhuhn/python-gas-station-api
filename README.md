# Python Tankstellen Api Wrapper 

Dies ist ein API Wrapper für Tankstellen in Deutschland. Als Quelle wird [TankerKönig](https://creativecommons.tankerkoenig.de/) verwendet.

## Getting started
1. API Key: </br>
    1. [API Key anlegen](https://creativecommons.tankerkoenig.de/) -> API-KEY </br>
    2. Neue Datei mit dem Namen `secret.txt` im Ordner der lib erstellen </br>
    3. Den API Key in die Datei kopieren. </br> </br>
2. SercretHandler: </br>
    1. Das Objekt secret vom secretHandler erstellen </br>
    2. Die Methode `loadFromSecret` ausführen. Damit wird die Datei `secret.txt` ausgelesen.
    3. Rückgabewerte: </br>
        0: Secret wurde geladen </br>
        1: Fehler beim Lesen von `secret.txt` </br> </br>
3. ApiHandler:
    1. api Objekt erstellen. Mit übergeben wird die Postleitzahl und das secret Objekt
    
# Libs
[pgeocode](https://pypi.org/project/pgeocode/)
[requests](https://pypi.org/project/requests/)
