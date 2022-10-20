from enum import Enum


class Mode(Enum):
    DUR = 1
    MOLL = 2

    def getFlats(self):
        if self == Mode.DUR: return [3, 7]
        if self == Mode.MOLL: return [2, 5]
