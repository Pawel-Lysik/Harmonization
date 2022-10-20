from subdominant import Subdominant
from chordSlice import ChordSlice
from chromatic import Chromatic
from harmonicSlice import HarmonicSlice
import copy


class Subdominant11 (Subdominant):
    def __init__(self, subdominant: Subdominant):
        super().__init__()
        self.ingredients = copy.copy(subdominant.ingredients)
        self.ingredients.insert(0, 1)
        self.chromatics = copy.copy(subdominant.chromatics)
        self.chromatics.insert(0, Chromatic.NEUTRAL)
        self.getDegrees()

    def harmonize(self, current: HarmonicSlice, prev: HarmonicSlice):
        self.defaultHarmonize(current, prev)

    def getChords(self, chordSlice: ChordSlice):
        self.basicGetChords(chordSlice)
