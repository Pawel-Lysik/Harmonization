from chordSlice import ChordSlice
from chromatic import Chromatic
from harmonicSlice import HarmonicSlice
from subdominant import Subdominant


class Subdominant55 (Subdominant):
    def __init__(self, subdominant: Subdominant):
        super().__init__()
        self.ingredients = subdominant.ingredients
        self.ingredients.append(5)
        self.chromatics = subdominant.chromatics
        self.chromatics.append(Chromatic.NEUTRAL)
        self.getDegrees()

    def harmonize(self, current: HarmonicSlice, prev: HarmonicSlice):
        self.defaultHarmonize(current, prev)

    def getChords(self, chordSlice: ChordSlice):
        self.basicGetChords(chordSlice)
