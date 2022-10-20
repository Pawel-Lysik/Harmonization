from enum import Enum


# metrum
class Metrum(Enum):
    RESTRICTED = 0
    STRONG = 1
    WEAK = 2
    FIRST = 3
    END = 4

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()
