import harmonicSlice

from harmonicFunction import HarmonicFunction
from chromatic import Chromatic


class SVI(HarmonicFunction):
    def __init__(self):
        super().__init__()
        self.prime = 6
        self.ingredients = [1, 1, 3, 5]
        self.chromatics = [Chromatic.NEUTRAL, Chromatic.NEUTRAL, Chromatic.NEUTRAL, Chromatic.NEUTRAL]
        self.getDegrees()
        self.bassBound = 1

    def harmonize(self, current: harmonicSlice.HarmonicSlice, prev: harmonicSlice.HarmonicSlice):
        self.harmonization(current, prev)
