from progression import Progression


class GeometricProgression(Progression):
    def __init__(self, base =2, start=1):
        super().__init__(start)
        self._base = base

        