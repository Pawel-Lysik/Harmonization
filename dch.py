from chromatic import Chromatic
from d7 import D7


class Dch (D7):
    def __init__(self):
        super().__init__()
        self.ingredients = [1, 3, 6, 7]
        self.chromatics = [Chromatic.NEUTRAL, Chromatic.HARMONIC, Chromatic.NEUTRAL, Chromatic.NEUTRAL]
        self.getDegrees()
        self.sopranBound = 6
