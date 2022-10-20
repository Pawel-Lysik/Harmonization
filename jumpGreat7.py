from chordBound import ChordBound
from pitch import Pitch
from sound import Sound


class JumpGreat7(ChordBound):
    @staticmethod
    def check(prev, chord, key = None):
        for i in range(4):
            if Pitch.getInterval(prev[i], chord[i]) == 7 and abs(Pitch.getIntervalBySemitones(prev[i], chord[i])) == 11: return False
        return True
