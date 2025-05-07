from animal import Animal

class Bird(Animal): 
    def reproduce(self) -> str:
        birdReproduce = 'Birds typically reproduce by hatching and incubating their eggs.'
        return super().reproduce() + birdReproduce

    def __repr__(self):
        birdInfo = '\nClass: Bird'
        return super().__repr__() + birdInfo
    