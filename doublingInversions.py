from harmonicBound import HarmonicBound
from harmonicSlice import HarmonicSlice
from keyDegree import KeyDegree


class DoublingInversions(HarmonicBound):
    @staticmethod
    def check(chord, harmonicSlice: HarmonicSlice):
        function = harmonicSlice.harmonicFunction
        key = harmonicSlice.mainSlice.key
        bass = chord[0]
        bassIngredient = function.getIngredient(KeyDegree.fromPitch(bass, key))

        doubling = None
        tempList = []
        for voice in chord:
            for tempV in tempList:
                if voice.degree == tempV.degree and voice.chromatic == tempV.chromatic:
                    doubling = voice
            else: tempList.append(voice)
        doublingIngredient = function.getIngredient(KeyDegree.fromPitch(doubling, key))

        if bassIngredient == 1 and doublingIngredient == 5: return False
        if bassIngredient == 5 and doublingIngredient == 1: return False
        return True
