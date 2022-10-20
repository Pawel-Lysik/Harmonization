import harmonicSlice

from harmonicFunction import HarmonicFunction
from chromatic import Chromatic


class DIII(HarmonicFunction):
    def __init__(self):
        super().__init__()
        self.prime = 3
        self.ingredients = [1, 3, 3, 5]
        self.chromatics = [Chromatic.NEUTRAL, Chromatic.NEUTRAL, Chromatic.NEUTRAL, Chromatic.HARMONIC]
        self.getDegrees()
        self.bassBound = 3

    def harmonize(self, current: harmonicSlice.HarmonicSlice, prev: harmonicSlice.HarmonicSlice):
        self.harmonization(current, prev)
