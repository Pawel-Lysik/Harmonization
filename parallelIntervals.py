from chordBound import ChordBound
from pitch import Pitch


class ParallelIntervals(ChordBound):
    @staticmethod
    def check(prev, chord, key = None):
        for i in range(4):
            for j in range(4):
                if prev[i] < prev[j]:
                    semitones = Pitch.getIntervalBySemitones(prev[i], prev[j])
                    complexInterval = Pitch.getComplexInterval(prev[i], prev[j])
                    if (complexInterval > 1 and semitones % 12 == 0) or semitones % 12 == 7:
                        iSemitones = Pitch.getIntervalBySemitones(prev[i], chord[i])
                        jSemitones = Pitch.getIntervalBySemitones(prev[j], chord[j])
                        if iSemitones == jSemitones and iSemitones != 0: return False
        return True
