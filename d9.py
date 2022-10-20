from chromatic import Chromatic
from trueNinth import TrueNinth
from d7 import D7


class D9 (D7):
    def __init__(self):
        super().__init__()
        self.ingredients = [1, 3, 7, 9]
        self.chromatics = [Chromatic.NEUTRAL, Chromatic.HARMONIC, Chromatic.NEUTRAL, Chromatic.NEUTRAL]
        self.harmonicBounds.append(TrueNinth)
        self.getDegrees()
