from abc import ABCMeta

class Pet(object, metaclass=ABCMeta):
    def __init__(self, legs = 0):
        self.legs = legs
        
    def pet(self) -> str:
        return (f'You can pet this animal')
    
    def __repr__(self)->str:
        return (f'This animal is a pet.')
    

    