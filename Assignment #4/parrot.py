from pet import Pet
from omnivore import Omnivore
from bird import Bird

class Parrot(Bird, Omnivore, Pet): 
    def __init__(self, legs = 2, wings= 2, color='yellow'):
        super().__init__(legs) # doesn't need self
        super().__init__(wings)
        self.color = color

    def __repr__(self):
        text = '\nSpecies: Parrot'
        result = Bird.__repr__(self) + text 
        result += '\n' + Pet.__repr__(self)  # Add Pet info
        result += '\n' + Omnivore.__repr__(self)  # Add Omnivore info
        return result
    
    def reproduce(self) -> None:
        mammal = Bird.reproduce(self)  # this must return a string
        dog = ' Parrots often take a few days to lay a full clutch of eggs. \
This can be as many as three to four eggs.'
        return mammal+dog

    def move(self) -> None:
        print('I can move in various ways. I can fly, walk, climb and even use a \
unique method called "beakiation" to traverse narrow branches.')

    def sleep(self) -> None:
        print('Parrots sleep around 10 to 12 houes each night, often tucked under their \
wings. They may also take naps during the day.')
        
    def eat(self) -> None:
        Omnivore.eat(self)
        print("I eat both plant and animal matter. My natural diet includes a variety of foods \
like seeds, nuts, fruits, vegetables, flowers, buds, and insects.")



# if __name__ == '__main__':
#     b1 = Parrot()
#     print()
#     print(repr(b1))
#     print()
#     print(b1.reproduce())
#     print()
#     b1.eat()
#     print()
#     b1.move()
#     print()
#     b1.sleep()
#     print()
#     print(b1.pet())
#     print()
