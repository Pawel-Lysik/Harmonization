from copy import copy

from sound import Sound


class Pitch:
    def __init__(self, octave: int, degree: Sound, chromatic: int = 0):
        self.octave = octave
        self.degree = degree
        self.chromatic = chromatic

    def __lt__(self, other):
        if self.octave != other.octave: return self.octave < other.octave
        if self.degree != other.degree: return self.degree < other.degree
        return self.chromatic < other.chromatic

    def __le__(self, other):
        if self.octave != other.octave: return self.octave < other.octave
        if self.degree != other.degree: return self.degree < other.degree
        return self.chromatic <= other.chromatic

    def __str__(self):
        chromaticName = ""
        if self.chromatic > 0:
            for i in range(self.chromatic): chromaticName = chromaticName + "is"
        if self.chromatic < 0:
            for i in range(-self.chromatic): chromaticName = chromaticName + "es"

        if self.chromatic < 0:
            if self.degree == Sound.A or self.degree == Sound.E:
                chromaticName = chromaticName[1:]
        if self.degree == Sound.H and self.chromatic == -1:
            return "B" + self.octave.__str__()
        return self.degree.__str__() + chromaticName + self.octave.__str__()

    def __eq__(self, other):
        return self.octave == other.octave and self.degree == other.degree and self.chromatic == other.chromatic

    def __hash__(self):
        return hash((self.octave, self.degree, self.chromatic))

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def getIntervalBySemitones(one, other):
        oneSemitones = one.octave * 12 + one.degree.value * 2 + one.chromatic
        otherSemitones = other.octave * 12 + other.degree.value * 2 + other.chromatic
        if one.degree.value >= Sound.F.value: oneSemitones -= 1
        if one.degree.value == Sound.H.value: oneSemitones -= 1
        if other.degree.value >= Sound.F.value: otherSemitones -= 1
        if other.degree.value == Sound.H.value: otherSemitones -= 1
        return oneSemitones - otherSemitones

    @staticmethod
    def getInterval(one, other):
        interval = abs(one.octave * 7 + one.degree.value - other.octave * 7 - other.degree.value) + 1
        interval = (interval + 6) % 7 + 1
        return interval

    @staticmethod
    def getComplexInterval(one, other):
        return abs(one.octave * 7 + one.degree.value - other.octave * 7 - other.degree.value) + 1
