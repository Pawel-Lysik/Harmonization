from key import Key
from pitch import Pitch


# array of possibilities for one measure of tact

class ChordSlice:
    def __init__(self, key: Key, voiceBounds):
        self.key = key
        self.voiceBounds = voiceBounds
        self.body = {}

    def set(self, S: Pitch, A: Pitch, T: Pitch, B: Pitch):
        chord = (B, T, A, S)
        if chord not in self.body:
            self.body[chord] = []

    def addChord(self, chord, prevSlice, pChord):
        chordTuple = tuple(chord)
        if chordTuple not in self.body:
            self.body[chordTuple] = [(prevSlice, pChord)]
        else:
            if (prevSlice, pChord) not in self.body[chordTuple]:
                self.body[chordTuple].append((prevSlice, pChord))

    def print(self):
        for k in self.body:
            print(f"{k}: {self.body[k]}")  #

    def __str__(self):
        return "sliceRef"

    def __repr__(self):
        return self.__str__()
