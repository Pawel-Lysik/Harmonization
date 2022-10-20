import itertools
from borderIngredientBounds import BorderIngredientBounds
from chordSlice import ChordSlice
from keyDegree import KeyDegree
from voiceBound import VoiceBound
from pitch import Pitch
from chromatic import Chromatic
from mode import Mode
from crossVoices import CrossVoices
from allVs1way import AllVoicesOneWay
from metrumInversions import MetrumInversions
from parallelIntervals import ParallelIntervals
from falseRelation import FalseRelation
from jumpGreat7 import JumpGreat7
from beyond8Jump import Beyond8Jump
from voiceBounds import VoiceBounds
import harmonicSlice
import basicFunction


class HarmonicFunction:
    def __init__(self):
        self.prime = 0
        self.bassBound = 0
        self.sopranBound = 0
        self.ingredients = []
        self.chromatics = []
        self.degrees = []
        self.chordBounds = [CrossVoices, AllVoicesOneWay, ParallelIntervals, FalseRelation, JumpGreat7, Beyond8Jump]
        self.harmonicBounds = [MetrumInversions, BorderIngredientBounds, VoiceBounds]

    def getDegrees(self):
        self.degrees = []
        for ing in self.ingredients:
            self.degrees.append((ing + self.prime - 2) % 7 + 1)

    def createStrict(self, chordSlice: ChordSlice, soprano: Pitch, chordComponent: KeyDegree, chordComponents: list, mapping):
        chordComponentIdx = chordComponents.index(chordComponent)
        ccSize = len(chordComponents)
        alt = chordComponents[(chordComponentIdx + mapping[0]) % ccSize].getPitch(soprano.octave)
        if soprano < alt: alt.octave = alt.octave - 1
        tenor = chordComponents[(chordComponentIdx + mapping[1]) % ccSize].getPitch(alt.octave)
        if alt < tenor: tenor.octave = tenor.octave - 1

        tempBassBound = VoiceBound(chordSlice.voiceBounds.B.bottom, tenor)
        bassVariants = tempBassBound.getVariants(KeyDegree(chordSlice.key, self.prime))
        for bass in bassVariants:
            chordSlice.set(soprano, alt, tenor, bass)

    def getChordComponents(self, chordSlice: ChordSlice):
        chordComponents = []
        for i in range(len(self.degrees)):
            if self.chromatics[i] == Chromatic.HARMONIC:
                chrSign = 1 if chordSlice.key.mode == Mode.MOLL else 0
            else:
                chrSign = self.chromatics[i].value
            chordComponents.append(KeyDegree(chordSlice.key, self.degrees[i], Chromatic(chrSign)))
        return chordComponents

    def fillSlice(self, chordSlice: ChordSlice):
        chordComponents = self.getChordComponents(chordSlice)
        for chordComponent in chordComponents:
            variants = chordSlice.voiceBounds.S.getVariants(chordComponent)
            for variant in variants:
                self.createStrict(chordSlice, variant, chordComponent, chordComponents, [2, 1])  # concentrated
                self.createStrict(chordSlice, variant, chordComponent, chordComponents, [1, 2])  # extensive

    def getIngredient(self, keyDegree: KeyDegree):
        return self.ingredients[self.degrees.index(keyDegree.degree)]

    def nearestWayConnection(self, current: harmonicSlice.HarmonicSlice, prev: harmonicSlice.HarmonicSlice, mapping: dict):
        chordSlice = current.mainSlice
        for prevSlice in [prev.mainSlice, prev.auxSlice]:
            for pChord in prevSlice.body:
                chord = []
                for pVoice in pChord:
                    pVoiceDegree = KeyDegree.fromPitch(pVoice, chordSlice.key)
                    idx = self.ingredients.index(mapping[prev.harmonicFunction.getIngredient(pVoiceDegree)])
                    keyDeg = KeyDegree(chordSlice.key, self.degrees[idx], self.chromatics[idx])
                    voice = keyDeg.getPitch(pVoice.octave)
                    if voice.degree - pVoice.degree > 4: voice.octave = voice.octave - 1
                    if pVoice.degree - voice.degree > 4: voice.octave = voice.octave + 1
                    chord.append(voice)

                bassIng = prev.harmonicFunction.getIngredient(KeyDegree.fromPitch(pChord[0], prev.mainSlice.key))
                if bassIng == 1:
                    tempBassBound = VoiceBound(chordSlice.voiceBounds.B.bottom, chord[1])
                    bassVariants = tempBassBound.getVariants(KeyDegree(chordSlice.key, self.prime, self.chromatics[0]))
                    for bass in bassVariants:
                        chord[0] = bass
                        if self.check(pChord, chord, current):
                            chordSlice.addChord(chord, prevSlice, pChord)
                else:
                    if not issubclass(type(prev.harmonicFunction), basicFunction.BasicFunction):
                        chordSlice.addChord(chord, prevSlice, pChord)

    def getChords(self, chordSlice: ChordSlice):
        chordComponents = self.getChordComponents(chordSlice)
        chordPermutations = list(itertools.permutations(chordComponents))
        for perm in chordPermutations:
            variants = chordSlice.voiceBounds.S.getVariants(perm[0])
            for sopran in variants:
                alt = perm[1].getPitch(sopran.octave)
                if sopran < alt: alt.octave = alt.octave - 1
                tenor = perm[2].getPitch(alt.octave)
                if alt < tenor: tenor.octave = tenor.octave - 1
                bass = perm[3].getPitch(tenor.octave)
                if tenor < bass: bass.octave = bass.octave - 1
                chordSlice.set(sopran, alt, tenor, bass)

    def harmonize(self, current: harmonicSlice.HarmonicSlice, prev: harmonicSlice.HarmonicSlice):
        pass

    def check(self, pChord, chord, hSlice: harmonicSlice.HarmonicSlice):
        for bound in self.chordBounds:
            if not bound.check(pChord, chord, hSlice.mainSlice.key):
                # print(pChord, chord, "connection is reject by", bound, "rule")
                return False
        for bound in self.harmonicBounds:
            if not bound.check(chord, hSlice):
                # print(pChord, chord, "connection is reject by", bound, "rule")
                return False
        return True

    def checkSlice(self, hSlice: harmonicSlice.HarmonicSlice):
        chordSlice = hSlice.mainSlice
        for chord in chordSlice.body:
            for pSlice, pChord in list(chordSlice.body[chord]):
                if not self.check(pChord, chord, hSlice):
                    chordSlice.body[chord].remove((pSlice, pChord))

    def basicHarmonization(self, current: harmonicSlice.HarmonicSlice, prev: harmonicSlice.HarmonicSlice, mapping):
        chordSlice = current.mainSlice
        self.getChords(chordSlice)
        for chord in chordSlice.body:
            baseIng = self.getIngredient(KeyDegree.fromPitch(chord[0], chordSlice.key))
            for pSlice in [prev.mainSlice, prev.auxSlice]:
                for pChord in pSlice.body:
                    pBaseIng = prev.harmonicFunction.getIngredient(KeyDegree.fromPitch(pChord[0], prev.mainSlice.key))
                    if baseIng == 1 and pBaseIng == 1: continue
                    if self.check(pChord, chord, current):
                        chordSlice.body[chord].append((pSlice, pChord))
        self.nearestWayConnection(current, prev, mapping)

    def harmonization(self, current: harmonicSlice.HarmonicSlice, prev: harmonicSlice.HarmonicSlice):
        chordSlice = current.mainSlice
        self.getChords(chordSlice)
        for chord in chordSlice.body:
            for pSlice in [prev.mainSlice, prev.auxSlice]:
                for pChord in pSlice.body:
                    if self.check(pChord, chord, current):
                        chordSlice.body[chord].append((pSlice, pChord))
