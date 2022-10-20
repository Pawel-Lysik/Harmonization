import basicFunction
import doublingInversions
import harmonicFunction
import harmonicSlice
import subdominant
import dominant
import d7not1
import d7
import s6
import mollDVII
import dIII
from chordSlice import ChordSlice
from chromatic import Chromatic
from keyDegree import KeyDegree


class Tonic (harmonicFunction.HarmonicFunction, basicFunction.BasicFunction):
    def __init__(self):
        super().__init__()
        self.prime = 1
        self.ingredients = [1, 3, 5]
        self.chromatics = [Chromatic.NEUTRAL, Chromatic.NEUTRAL, Chromatic.NEUTRAL, Chromatic.NEUTRAL]
        self.getDegrees()
        self.harmonicBounds.append(doublingInversions.DoublingInversions)

    def d7solutionFree(self, current: harmonicSlice, prev: harmonicSlice.HarmonicSlice):
        self.nearestWayConnection(current, prev, {1: 5, 3: 1, 5: 3, 7: 5})

    def d7not1SolutionFree(self, chordSlice: ChordSlice, prev: harmonicSlice.HarmonicSlice):
        mapping = {3: 1, 7: 5}
        fifth = 0
        solution = [1, 3]
        for i in range(len(solution)):
            for prevSlice in [prev.mainSlice, prev.auxSlice]:
                for pChord in prevSlice.body:
                    chord = []
                    for pVoice in pChord:
                        pVoiceDegree = KeyDegree.fromPitch(pVoice, chordSlice.key)
                        pVoiceIngredient = prev.harmonicFunction.getIngredient(pVoiceDegree)
                        if pVoiceIngredient == 5:
                            idx = self.ingredients.index(solution[(i + fifth) % len(solution)])
                            fifth = fifth + 1
                        else: idx = self.ingredients.index(mapping[pVoiceIngredient])
                        keyDeg = KeyDegree(chordSlice.key, self.degrees[idx], self.chromatics[idx])
                        voice = keyDeg.getPitch(pVoice.octave)
                        if voice.degree - pVoice.degree > 4: voice.octave = voice.octave - 1
                        if pVoice.degree - voice.degree > 4: voice.octave = voice.octave + 1
                        chord.append(voice)
                    chordSlice.addChord(chord, prevSlice, pChord)

    def d7not1SolutionStrict(self, chordSlice: ChordSlice, prev: harmonicSlice.HarmonicSlice):
        mapping = {3: 1, 5: 5, 7: 3}
        for prevSlice in [prev.mainSlice, prev.auxSlice]:
            for pChord in prevSlice.body:
                chord = []
                for i in range(4):
                    pVoice = pChord[i]
                    pVoiceDegree = KeyDegree.fromPitch(pVoice, chordSlice.key)
                    pIngredient = prev.harmonicFunction.getIngredient(pVoiceDegree)
                    if i == 0 and pIngredient == 5: idx = self.ingredients.index(5)
                    else: idx = self.ingredients.index(mapping[pIngredient])
                    keyDeg = KeyDegree(chordSlice.key, self.degrees[idx], self.chromatics[idx])
                    voice = keyDeg.getPitch(pVoice.octave)
                    if voice.degree - pVoice.degree > 4: voice.octave = voice.octave - 1
                    if pVoice.degree - voice.degree > 4: voice.octave = voice.octave + 1
                    chord.append(voice)
                chordSlice.addChord(chord, prevSlice, pChord)

    def defaultHarmonize(self, current: harmonicSlice.HarmonicSlice, prev: harmonicSlice.HarmonicSlice):
        chordSlice = current.mainSlice
        if type(prev.harmonicFunction) == s6.S6:
            prev.harmonicFunction.connection(self, chordSlice, prev)
            return

        if issubclass(type(prev.harmonicFunction), subdominant.Subdominant):
            self.basicHarmonization(current, prev, {1: 3, 3: 5, 5: 1})
            return

        if type(prev.harmonicFunction) == d7not1.D7not1:
            self.d7not1SolutionFree(chordSlice, prev)
            self.d7not1SolutionStrict(chordSlice, prev)
            return

        if issubclass(type(prev.harmonicFunction), d7.D7):
            self.nearestWayConnection(current, prev, {1: 5, 3: 1, 5: 1, 6: 1, 7: 3, 9: 5})
            if type(prev.harmonicFunction) == d7.D7: self.d7solutionFree(current, prev)
            return

        if issubclass(type(prev.harmonicFunction), dominant.Dominant):
            self.basicHarmonization(current, prev, {1: 5, 3: 1, 5: 3})
            return

        if issubclass(type(prev.harmonicFunction), Tonic):
            self.harmonization(current, prev)
            return

        if type(prev.harmonicFunction) in [mollDVII.MollDVII, dIII.DIII]:
            self.harmonization(current, prev)
            return

    def harmonize(self, current: harmonicSlice.HarmonicSlice, prev: harmonicSlice.HarmonicSlice):
        tonic11.Tonic11().harmonize(current, prev)
        tonic55.Tonic55().harmonize(current, prev)
        self.checkSlice(current)

    def basicGetChords(self, chordSlice: ChordSlice):
        super().getChords(chordSlice)

    def getChords(self, chordSlice: ChordSlice):
        tonic11.Tonic11().getChords(chordSlice)
        tonic55.Tonic55().getChords(chordSlice)


import tonic11
import tonic55
