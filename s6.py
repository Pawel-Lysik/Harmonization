import harmonicFunction
from chromatic import Chromatic
from key import Key
from harmonicSlice import HarmonicSlice
from harmonicFunction import HarmonicFunction
from keyDegree import KeyDegree


class S6 (HarmonicFunction):
    def __init__(self):
        super().__init__()
        self.prime = 4
        self.ingredients = [1, 3, 5, 6]
        self.chromatics = [Chromatic.NEUTRAL, Chromatic.NEUTRAL, Chromatic.NEUTRAL, Chromatic.NEUTRAL]
        self.getDegrees()

    def up6check(self, pChord, chord, key: Key):
        for i in range(4):
            if self.getIngredient(KeyDegree.fromPitch(pChord[i], key)) == 6:
                if chord[i] < pChord[i]: return False
        return True

    def harmonize(self, current: HarmonicSlice, prev: HarmonicSlice):
        chordSlice = current.mainSlice
        self.getChords(chordSlice)
        for chord in chordSlice.body:
            for pSlice in [prev.mainSlice, prev.auxSlice]:
                for pChord in pSlice.body:
                    if self.check(pChord, chord, current):
                        chordSlice.body[chord].append((pSlice, pChord))

    def connection(self, function: HarmonicFunction, current: HarmonicSlice, prev: HarmonicSlice):
        chordSlice = current.mainSlice
        function.getChords(chordSlice)
        for chord in chordSlice.body:
            for pSlice in [prev.mainSlice, prev.auxSlice]:
                for pChord in pSlice.body:
                    if function.check(pChord, chord, current) and self.up6check(pChord, chord, prev.mainSlice.key):
                        chordSlice.body[chord].append((pSlice, pChord))

