import doublingInversions
from chordSlice import ChordSlice
from chromatic import Chromatic
from harmonicSlice import HarmonicSlice
import harmonicFunction
import basicFunction
import tonic
import tIII
import tVI


class Subdominant (harmonicFunction.HarmonicFunction, basicFunction.BasicFunction):
    def __init__(self):
        super().__init__()
        self.prime = 4
        self.ingredients = [1, 3, 5]
        self.chromatics = [Chromatic.NEUTRAL, Chromatic.NEUTRAL, Chromatic.NEUTRAL]
        self.getDegrees()
        self.harmonicBounds.append(doublingInversions.DoublingInversions)

    def defaultHarmonize(self, current: HarmonicSlice, prev: HarmonicSlice):
        if issubclass(type(prev.harmonicFunction), tonic.Tonic):
            self.basicHarmonization(current, prev, {1: 5, 3: 1, 5: 3})

        if type(prev.harmonicFunction) == Subdominant:
            self.harmonization(current, prev)

        if type(prev.harmonicFunction) in [tIII.TIII, tVI.TVI]:
            self.harmonization(current, prev)

    def harmonize(self, current: HarmonicSlice, prev: HarmonicSlice):
        import subdominant11
        import subdominant55
        subdominant11.Subdominant11(self).harmonize(current, prev)
        subdominant55.Subdominant55(self).harmonize(current, prev)
        self.checkSlice(current)

    def basicGetChords(self, chordSlice: ChordSlice):
        super().getChords(chordSlice)

    def getChords(self, chordSlice: ChordSlice):
        subdominant11.Subdominant11(self).getChords(chordSlice)
        subdominant55.Subdominant55(self).getChords(chordSlice)


import subdominant11
import subdominant55
