from heterotroph import Heterotroph

class Herbivore(Heterotroph):
    def eat(self):
        super().eat()
        print("I eat plants")

    def __repr__(self)->str:
        return (f"{super().__repr__()}\nThis organism is herbivore. It feeds on plant matter and its physiology facilitates food serach.")
    
    