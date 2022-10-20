from chordBound import ChordBound


class CrossVoices(ChordBound):
    @staticmethod
    def check(prev, chord, key = None):
        B, T, A, S = chord[0], chord[1], chord[2], chord[3]
        pB, pT, pA, pS = prev[0], prev[1], prev[2], prev[3]
        if T < pB or A < pT or S < pA or pT < B or pA < T or pS < A: return False
        return True
