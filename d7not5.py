from chromatic import Chromatic
from d7 import D7


class D7not5 (D7):
    def __init__(self):
        super().__init__()
        self.ingredients = [1, 1, 3, 7]
        self.chromatics = [Chromatic.NEUTRAL, Chromatic.NEUTRAL, Chromatic.HARMONIC, Chromatic.NEUTRAL]
        self.getDegrees()
