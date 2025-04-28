from mammal import Mammal
from pet import Pet
from herbivore import Herbivore

class Bunny(Mammal, Herbivore, Pet):
    def __init__(self, legs = 4, ears = 2):
        super().__init__(legs)
        # Mammal.__init__(self, legs)
        self.ears = ears

    def __repr__(self):
        return Mammal.__repr__(self)+"\nSpecies: Bunny\n"+Pet.__repr__(self)+'\n'+Herbivore.__repr__(self)
    

    def reproduce(self)->None:
        super().reproduce()
        print('Bunnies can produce multiple litters per year potentially having 3-8 kits per litter')


    def sleep(self):
        print("Bunnies as nocturnal animals, typically sleep around 12 to 14 hours a day in short, intermitten periods")

    def eat(self):
        Herbivore.eat(self)
        print("I mostly eat fresh hay and grass with some leafy greens and a few pellets. I should only be given fruits and brute vegetables, like carrots as an occasional treat.")


if __name__ == "__main__":
    b1 = Bunny()
    print(b1)

    print()
    b1.sleep()

    print()
    b1.eat()

    print()
    print(b1.pet())