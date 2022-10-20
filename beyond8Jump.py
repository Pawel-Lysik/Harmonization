from chordBound import ChordBound
from pitch import Pitch


class Beyond8Jump(ChordBound):
    @staticmethod
    def check(prev, chord, key = None):
        for i in range(4):
            if Pitch.getComplexInterval(prev[i], chord[i]) > 8: return False
        return True
