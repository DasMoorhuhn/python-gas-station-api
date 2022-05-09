class secret:
    def __init__(self) -> None:
        self.__apiKey = ""

    def setApiKey(self, apiKey:str):
        self.__apiKey = apiKey

    def getApiKey(self):
        return self.__apiKey

    def loadFromSecret(self):
        with open(file="secret.txt", mode="r") as file:
            try:
                self.setApiKey(str(file.readlines()[0].strip("\n")))
                return 0
            except:
                return 1