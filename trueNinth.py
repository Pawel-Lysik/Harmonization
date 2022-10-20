from harmonicBound import HarmonicBound
from keyDegree import KeyDegree
from pitch import Pitch


class TrueNinth(HarmonicBound):
    @staticmethod
    def check(chord, harmonicSlice):
        function = harmonicSlice.harmonicFunction
        key = harmonicSlice.mainSlice.key
        prime = None
        ninth = None
        for note in chord:
            if function.getIngredient(KeyDegree.fromPitch(note, key)) == 1: prime = note
            if function.getIngredient(KeyDegree.fromPitch(note, key)) == 9: ninth = note

        if prime is None: return True
        if Pitch.getComplexInterval(prime, ninth) == 9: return True
        return False
