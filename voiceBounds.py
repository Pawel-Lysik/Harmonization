from voiceBound import VoiceBound
from harmonicBound import HarmonicBound
from harmonicSlice import HarmonicSlice


class VoiceBounds(HarmonicBound):
    def __init__(self, B: VoiceBound, T: VoiceBound, A: VoiceBound, S: VoiceBound):
        self.B = B
        self.T = T
        self.A = A
        self.S = S

    def checkChord(self, chord):
        B, T, A, S = chord[0], chord[1], chord[2], chord[3]
        if B < self.B.bottom or self.B.top < B: return False
        if T < self.T.bottom or self.T.top < T: return False
        if A < self.A.bottom or self.A.top < A: return False
        if S < self.S.bottom or self.S.top < S: return False
        return True

    @staticmethod
    def check(chord, harmonicSlice: HarmonicSlice):
        return harmonicSlice.voiceBounds.checkChord(chord)
