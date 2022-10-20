from keyDegree import KeyDegree
from harmonicSlice import HarmonicSlice
from harmonicBound import HarmonicBound
from metrum import Metrum


class MetrumInversions(HarmonicBound):
    @staticmethod
    def check(chord, harmonicSlice: HarmonicSlice):
        bass = chord[0]
        function = harmonicSlice.harmonicFunction
        key = harmonicSlice.mainSlice.key
        bassIngredient = function.getIngredient(KeyDegree.fromPitch(bass, key))
        metrum = harmonicSlice.metrum
        if bassIngredient == 5 and (metrum == Metrum.FIRST or metrum == Metrum.STRONG): return False
        return True
