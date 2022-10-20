from chordSlice import ChordSlice
from crossVoices import CrossVoices
from key import Key


class HarmonicSlice:
    def __init__(self, key: Key, voiceBounds, harmonicFunction, metrum, isFirst = False, isLast = False):
        self.voiceBounds = voiceBounds
        self.mainSlice = ChordSlice(key, voiceBounds)
        self.auxSlice  = ChordSlice(key, voiceBounds)
        self.harmonicFunction = harmonicFunction
        self.metrum = metrum
        self.isFirst = isFirst
        self.isLast = isLast
        self.sopranBound = 0
        self.bassBound = 0

    def harmonize(self, prev = None):
        if prev is None:
            self.harmonicFunction.fillSlice(self.mainSlice)
            for chord in list(self.mainSlice.body):
                for bound in self.harmonicFunction.harmonicBounds:
                    if not bound.check(chord, self):
                        if chord in self.mainSlice.body: self.mainSlice.body.pop(chord)
        else:
            self.harmonicFunction.harmonize(self, prev)

        if not self.isFirst:
            for chord in list(self.mainSlice.body):
                if not self.mainSlice.body[chord]: del self.mainSlice.body[chord]

        if not self.isLast: self.changePosition()

    def changePosition(self):
        self.harmonicFunction.getChords(self.auxSlice)

        for chord in self.auxSlice.body:
            for pChord in self.mainSlice.body:
                if CrossVoices.check(pChord, chord):
                    self.auxSlice.body[chord].append((self.mainSlice, pChord))

        for chord in list(self.auxSlice.body):
            if not self.auxSlice.body[chord]: del self.auxSlice.body[chord]

    def print(self):
        self.mainSlice.print()
        self.auxSlice.print()
