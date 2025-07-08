class Dog:

    species = "dog"

    def __init__(self, colour, breed, name):
        self.breed = breed
        self.name = name
        self.colour = colour

Max = Dog("Max", "German Shepard", "Brown")
Sprinke = Dog("Sprinke", "Dalmatian", "Red")

print("Max is a {}".format(Max.species))
print("Sprinke is also a {} too".format(Sprinke.species))

print("Max is a {}".format(Max.breed))
print("Sprinke is different from Max she is a {}".format(Sprinke.breed))