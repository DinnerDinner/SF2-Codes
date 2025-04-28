from animal import Animal

class Mammal(Animal):
    def reproduce(self):
        result = "Mammals give birth to live young and raise them until they can be indepednent."
    
        super().reproduce()
        print(result)


    def __repr__(self):
        text = "\nClass: Mammal"
        return super().__repr__() + text
    

    