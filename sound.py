from enum import Enum


class Sound(Enum):
    C = 1
    D = 2
    E = 3
    F = 4
    G = 5
    A = 6
    H = 7

    def __sub__(self, other):
        return self.value - other.value

    def __str__(self):
        return self.name

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def code(self):
        if self == Sound.H: return "B"
        return self.name
