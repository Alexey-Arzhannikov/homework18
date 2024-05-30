class Building:
    def __init__(self, name, floor):
        self.numberOfFloors = floor
        self.buildingType = name

    def __eq__(self, other):
        return self.buildingType == other.buildingType and self.numberOfFloors == other.numberOfFloors


h1 = Building('ЖК Университетский', 5)
h2 = Building('ЖК Победа', 10)
h3 = Building('ЖК Университетский', 5)
print(h1 == h2)
print(h1 == h3)
