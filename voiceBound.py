from copy import copy

from pitch import Pitch
from sound import Sound
from keyDegree import KeyDegree


# Range of voice
class VoiceBound:
    def __init__(self, bottom: Pitch, top: Pitch):
        self.bottom = bottom
        self.top = top

    def voiceRange(self):
        topVal = self.top.octave * 7 + self.top.degree.value
        bottomVal = self.bottom.octave * 7 + self.bottom.degree.value
        return topVal - bottomVal + 1

    def getVariants(self, keyDegree: KeyDegree):
        variants = []
        variant = keyDegree.getPitch(self.bottom.octave)

        if variant < self.bottom: variant.octave = variant.octave + 1
        while variant <= self.top:
            variants.append(copy(variant))
            variant.octave = variant.octave + 1
        return variants

    def getPosition(self, pitch: Pitch) -> int:
        semitones = (pitch.octave - self.bottom.octave) * 12 + (pitch.degree - self.bottom.degree) * 2 + pitch.chromatic - self.bottom.chromatic

        # take care of semitone between E and F
        if self.bottom.degree < pitch.degree and self.bottom.degree <= Sound.E and Sound.F <= pitch.degree:
            semitones = semitones - 1
        if pitch.degree < self.bottom.degree and pitch.degree <= Sound.E and Sound.F <= self.bottom.degree:
            semitones = semitones - 1

        # take care of semitone between H and C
        if self.bottom.degree < pitch.degree and self.bottom.degree <= Sound.H and Sound.C <= pitch.degree:
            semitones = semitones - 1
        if pitch.degree < self.bottom.degree and pitch.degree <= Sound.H and Sound.C <= self.bottom.degree:
            semitones = semitones - 1

        return semitones
