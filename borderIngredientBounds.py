from harmonicBound import HarmonicBound
from harmonicSlice import HarmonicSlice
from keyDegree import KeyDegree


class BorderIngredientBounds(HarmonicBound):
    @staticmethod
    def check(chord, harmonicSlice: HarmonicSlice):
        if harmonicSlice.bassBound == 0 and harmonicSlice.sopranBound == 0: return True
        function = harmonicSlice.harmonicFunction
        key = harmonicSlice.mainSlice.key
        bassIngredient = function.getIngredient(KeyDegree.fromPitch(chord[0], key))
        sopranIngredient = function.getIngredient(KeyDegree.fromPitch(chord[3], key))
        if harmonicSlice.bassBound != 0 and harmonicSlice.bassBound != bassIngredient: return False
        if harmonicSlice.sopranBound != 0 and harmonicSlice.sopranBound != sopranIngredient: return False
        return True
