import harmonicSlice
import d7
from harmonicFunction import HarmonicFunction
from chromatic import Chromatic


class MollTVIobn(HarmonicFunction):
    def __init__(self):
        super().__init__()
        self.prime = 6
        self.ingredients = [1, 3, 3, 5]
        self.chromatics = [Chromatic.FLAT, Chromatic.NEUTRAL, Chromatic.NEUTRAL, Chromatic.FLAT]
        self.getDegrees()
        self.bassBound = 1

    def harmonize(self, current: harmonicSlice.HarmonicSlice, prev: harmonicSlice.HarmonicSlice):
        chordSlice = current.mainSlice

        if issubclass(type(prev.harmonicFunction), d7.D7):
            self.nearestWayConnection(current, prev, {1: 1, 3: 3, 5: 3, 6: 3, 7: 5})
            self.checkSlice(current)
            return

        self.harmonization(current, prev)
