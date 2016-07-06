class PartyAnimal:

    x = 0
    name = ""

    def __init__(self, x):
        print("I am constructed with " + str(x))
        self.name = x

    def party(self):
        self.x += 1
        print("So far " + str(self.x))

    def __del__(self):
        print("I am destructed at " + str(self.x))


class FootballFan(PartyAnimal):

    points = 0

    def touchdown(self):
        self.points += 7
        self.party()
        print(self.name + "points " + self.points)

animal = PartyAnimal(x=4)

animal.party()
animal.party()
PartyAnimal.party(animal)
