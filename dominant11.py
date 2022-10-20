import dominant
from chordSlice import ChordSlice
from chromatic import Chromatic
import harmonicSlice


class Dominant11 (dominant.Dominant):
    def __init__(self):
        super().__init__()
        self.ingredients = [1, 1, 3, 5]
        self.chromatics = [Chromatic.NEUTRAL, Chromatic.NEUTRAL, Chromatic.HARMONIC, Chromatic.NEUTRAL]
        self.getDegrees()

    def harmonize(self, current: harmonicSlice.HarmonicSlice, prev: harmonicSlice.HarmonicSlice):
        self.defaultHarmonize(current, prev)

    def getChords(self, chordSlice: ChordSlice):
        self.basicGetChords(chordSlice)