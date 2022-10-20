import harmonicSlice

from harmonicFunction import HarmonicFunction
from chromatic import Chromatic
from allVs1way import AllVoicesOneWay


class SII(HarmonicFunction):
    def __init__(self):
        super().__init__()
        self.prime = 2
        self.ingredients = [1, 3, 3, 5]
        self.chromatics = [Chromatic.NEUTRAL, Chromatic.NEUTRAL, Chromatic.NEUTRAL, Chromatic.NEUTRAL]
        self.getDegrees()
        self.chordBounds.remove(AllVoicesOneWay)
        self.bassBound = 3

    def harmonize(self, current: harmonicSlice.HarmonicSlice, prev: harmonicSlice.HarmonicSlice):
        self.harmonization(current, prev)
