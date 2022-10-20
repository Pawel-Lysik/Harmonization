from chromatic import Chromatic
from mode import Mode
from sound import Sound
import keyDegree

class Key:
    def __init__(self, keyDegree: Sound, mode: Mode, chromatic: Chromatic = Chromatic.NEUTRAL):
        self.keyDegree = keyDegree
        self.mode = mode
        self.chromatic = chromatic

    def getFifths(self):
        fifths = 0
        for i in range(1, 8):
            fifths += keyDegree.KeyDegree(self, i).getPitch(2).chromatic
        return fifths
