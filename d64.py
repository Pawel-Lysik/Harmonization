from chromatic import Chromatic
from harmonicFunction import HarmonicFunction
from harmonicSlice import HarmonicSlice
import s6


class D64(HarmonicFunction):
    def __init__(self):
        super().__init__()
        self.prime = 5
        self.ingredients = [1, 1, 4, 6]
        self.chromatics = [Chromatic.NEUTRAL, Chromatic.NEUTRAL, Chromatic.NEUTRAL, Chromatic.NEUTRAL]
        self.getDegrees()

    def harmonize(self, current: HarmonicSlice, prev: HarmonicSlice):
        if type(prev.harmonicFunction) == s6.S6:
            if type(prev.harmonicFunction) == s6.S6:
                s6function = prev.harmonicFunction
                s6function.connection(self, current, prev)
        else: self.harmonization(current, prev)
