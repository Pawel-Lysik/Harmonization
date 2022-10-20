from chordBound import ChordBound
from keyDegree import KeyDegree


class FalseRelation(ChordBound):
    @staticmethod
    def check(prev, chord, key = None):
        if key is None: raise Exception("key is None")
        for i in range(4):
            for j in range(4):
                if i != j:
                    keyDegree1 = KeyDegree.fromPitch(prev[i], key)
                    keyDegree2 = KeyDegree.fromPitch(chord[j], key)
                    if keyDegree1.degree == keyDegree2.degree:
                        if abs(keyDegree1.chromatic.value - keyDegree2.chromatic.value) == 1: return False
        return True
