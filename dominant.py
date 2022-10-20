from chordSlice import ChordSlice
from chromatic import Chromatic
from keyDegree import KeyDegree
import harmonicSlice
import harmonicFunction
import doublingInversions
import basicFunction
import tonic
import subdominant
import s6
import d64
import sVI
import sII
import sN


class Dominant (harmonicFunction.HarmonicFunction, basicFunction.BasicFunction):
    def __init__(self):
        super().__init__()
        self.prime = 5
        self.ingredients = [1, 3, 5]
        self.chromatics = [Chromatic.NEUTRAL, Chromatic.HARMONIC, Chromatic.NEUTRAL]
        self.getDegrees()
        self.harmonicBounds.append(doublingInversions.DoublingInversions)

    def counterMovementConnection(self, chordSlice: ChordSlice, prev: harmonicSlice.HarmonicSlice):
        mapping = {1: 5, 3: 1, 5: 3}  # 1. S -> 5. D, 3. S -> 1. D, 5. S -> 3. D
        for prevSlice in [prev.mainSlice, prev.auxSlice]:
            for pChord in prevSlice.body:
                pB, pT, pA, pS = pChord[0], pChord[1], pChord[2], pChord[3]
                B = KeyDegree(chordSlice.key, self.prime).getPitch(pB.octave)
                if B < pB: B.octave = B.octave + 1
                chord = [B]
                for pVoice in (pT, pA, pS):
                    pVoiceDegree = KeyDegree.fromPitch(pVoice, chordSlice.key)
                    idx = self.ingredients.index(mapping[prev.harmonicFunction.getIngredient(pVoiceDegree)])
                    voice = KeyDegree(chordSlice.key, self.degrees[idx], self.chromatics[idx]).getPitch(pVoice.octave)
                    if pVoice < voice: voice.octave = voice.octave - 1
                    chord.append(voice)

                chord = tuple(chord)
                if chord not in chordSlice.body:
                    chordSlice.body[chord] = [(prevSlice, pChord)]
                else:
                    chordSlice.body[chord].append((prevSlice, pChord))

    def defaultHarmonize(self, current: harmonicSlice.HarmonicSlice, prev: harmonicSlice.HarmonicSlice):
        chordSlice = current.mainSlice
        if issubclass(type(prev.harmonicFunction), tonic.Tonic):
            self.basicHarmonization(current, prev, {1: 3, 3: 5, 5: 1})
        if issubclass(type(prev.harmonicFunction), subdominant.Subdominant):
            self.counterMovementConnection(chordSlice, prev)
        if type(prev.harmonicFunction) == s6.S6:
            s6function = prev.harmonicFunction
            s6function.connection(self, current, prev)
        if type(prev.harmonicFunction) == d64.D64:
            self.nearestWayConnection(current, prev, {1: 1, 4: 3, 6: 5})

        if type(prev.harmonicFunction) == Dominant:
            self.harmonization(current, prev)

        if type(prev.harmonicFunction) in [sII.SII, sVI.SVI, sN.SN]:
            self.harmonization(current, prev)

    def harmonize(self, current: harmonicSlice.HarmonicSlice, prev: harmonicSlice.HarmonicSlice):
        import dominant11
        import dominant55
        dominant11.Dominant11().harmonize(current, prev)
        dominant55.Dominant55().harmonize(current, prev)
        self.checkSlice(current)

    def basicGetChords(self, chordSlice: ChordSlice):
        super().getChords(chordSlice)

    def getChords(self, chordSlice: ChordSlice):
        dominant11.Dominant11().getChords(chordSlice)
        dominant55.Dominant55().getChords(chordSlice)


import dominant11
import dominant55
