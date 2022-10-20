from chromatic import Chromatic
from mode import Mode
from sound import Sound
from pitch import Pitch


class KeyDegree:
    def __init__(self, key, degree: int, chromatic=Chromatic.NEUTRAL):
        self.key = key
        self.degree = degree
        self.chromatic = chromatic

    def __str__(self):
        return self.degree.__str__() + self.chromatic.name

    def __repr__(self):
        return self.__str__()

    # unused
    def up(self, interval, chrChange=Chromatic.NEUTRAL):
        interval = interval - 1
        degree = self.degree + interval
        chromatic = Chromatic(self.chromatic.value + chrChange.value)
        return KeyDegree(self.key, degree, chromatic)

    def getPitch(self, octave: int):
        degOnScale = self.key.keyDegree.value
        sound = Sound((degOnScale + self.degree + 5) % 7 + 1)
        chrVal = self.key.chromatic.value
        semitones = self.key.mode.getFlats()

        for i in range(1, (sound.value - degOnScale + 7) % 7 + 1):
            if i in semitones:
                chrVal = chrVal - 1

            if (i + degOnScale + 5) % 7 + 1 == Sound.E.value or (i + degOnScale + 5) % 7 + 1 == Sound.H.value:
                chrVal = chrVal + 1

        if self.chromatic == Chromatic.HARMONIC:
            chrVal = chrVal + (self.key.mode == Mode.MOLL)
        else: chrVal = chrVal + self.chromatic.value

        return Pitch(octave, sound, chrVal)

    @staticmethod
    def fromPitch(pitch: Pitch, key):
        degree = (pitch.degree - key.keyDegree + 7) % 7 + 1
        chromatic = Chromatic(pitch.chromatic - KeyDegree(key, degree).getPitch(2).chromatic)
        return KeyDegree(key, degree, chromatic)
