from pet import Pet
from herbivore import Herbivore
from mammal import Mammal

class Bunny(Mammal, Herbivore, Pet):
    def __init__(self, legs = 4, ears = 2):
        super().__init__(legs) # doesn't need self
        self.ears = ears


    def __repr__(self):
        text = '\nSpecies: Bunny'
        result = Mammal.__repr__(self) + text  # Add Mammal info
        result += '\n' + Pet.__repr__(self)  # Add Pet info
        result += '\n' + Herbivore.__repr__(self)  # Add Herbivore info
        return result
    
    def reproduce(self) -> None:
        mammal = Mammal.reproduce(self)  
        bunny = 'Bunnies can produce multiple litters per year, potentially having 3–8 kits per litter.'
        return(mammal+bunny)

    def move(self) -> None:
        print('I move by hopping and I can see things behind me...')

    def sleep(self) -> None:
        print('Bunnies as nocturnal animals, typically sleep \
around 12 to 14 hours a day in short, intermittent periods')
        
    def eat(self) -> None:
        Herbivore.eat(self)
        print('I mostly eat fresh hay and grass, with some leafy greens and a \
few pellets. I should only be given fruit and root vegetables, like carrots, as occassional treat.')

