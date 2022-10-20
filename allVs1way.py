from chordBound import ChordBound


class AllVoicesOneWay(ChordBound):
    @staticmethod
    def check(prev, chord, key = None):
        ups = 0
        downs = 0
        for i in range(len(chord)):
            if prev[i] < chord[i]: ups = ups + 1
            if prev[i] > chord[i]: downs = downs + 1
        if ups == 4 or downs == 4: return False
        return True
