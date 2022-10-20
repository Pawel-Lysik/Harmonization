from chromatic import Chromatic
import d9


class D9not1(d9.D9):
    def __init__(self):
        super().__init__()
        self.ingredients = [3, 5, 7, 9]
        self.chromatics = [Chromatic.HARMONIC, Chromatic.NEUTRAL, Chromatic.NEUTRAL, Chromatic.NEUTRAL]
        self.getDegrees()
