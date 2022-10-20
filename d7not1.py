from chromatic import Chromatic
from d7 import D7


class D7not1 (D7):
    def __init__(self):
        super().__init__()
        self.ingredients = [3, 5, 5, 7]
        self.chromatics = [Chromatic.HARMONIC, Chromatic.NEUTRAL, Chromatic.NEUTRAL, Chromatic.NEUTRAL]
        self.getDegrees()
