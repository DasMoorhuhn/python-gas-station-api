class gasSation:
    def __init__(self, value:dict) -> None:
        self.id = value["id"]
        self.name = value["name"]
        self.brand = value["brand"]
        self.street = value["street"]
        self.houseNumber = value["houseNumber"]
        self.postCode = value["postCode"]
        self.place = value["place"]
        self.lat = value["lat"]
        self.lng = value["lng"]
        self.dist = value["dist"]
        self.diesel = value["diesel"]
        self.e5 = value["e5"]
        self.e10 = value["e10"]
        self.isOpen = value["isOpen"]

class city:
    def __init__(self, lat, lng, name, postalCode, communityCode) -> None:
        self.lat = lat
        self.lng = lng
        self.name = name
        self.postalCode = int(postalCode)
        self.communityCode = communityCode