import harmonicFunction
from chromatic import Chromatic
from harmonicSlice import HarmonicSlice
import s6


class D7 (harmonicFunction.HarmonicFunction):
    def __init__(self):
        super().__init__()
        self.prime = 5
        self.ingredients = [1, 3, 5, 7]
        self.chromatics = [Chromatic.NEUTRAL, Chromatic.HARMONIC, Chromatic.NEUTRAL, Chromatic.NEUTRAL]
        self.getDegrees()

    def harmonize(self, current: HarmonicSlice, prev: HarmonicSlice):
        if type(prev.harmonicFunction) == s6.S6:
            if type(prev.harmonicFunction) == s6.S6:
                s6function = prev.harmonicFunction
                s6function.connection(self, current, prev)
        else: self.harmonization(current, prev)
