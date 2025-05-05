from progression import Progression

class FibonacciProgression(Progression):
    def __init__(self, f1=0, f2=1):
        super().__init__(f1)
        self._prev = f2-f1