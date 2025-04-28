from abc import ABCMeta

class Heterotroph(object, metaclass = ABCMeta):
    def __init__(self, legs = 0, fins = 0, wings = 0):
        self.legs= legs
        self.fins = fins
        self.wings = wings

    def eat(self):
        print("I eat other organisms instead of producing my own food.")

    def __repr__(self)->str:
        return (f"This organism is a hetetotroph, it is unable to produce its own food, so it eats other organisms")
    
    