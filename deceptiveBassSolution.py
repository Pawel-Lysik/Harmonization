from chordBound import ChordBound
from pitch import Pitch


class DeceptiveBassSolution(ChordBound):
    @staticmethod
    def check(prev, chord, key = None):
        return Pitch.getComplexInterval(prev[0], chord[0]) == 2
