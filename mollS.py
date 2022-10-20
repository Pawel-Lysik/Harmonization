from chromatic import Chromatic
from subdominant import Subdominant


class MollS(Subdominant):
    def __init__(self):
        super().__init__()
        self.chromatics = [Chromatic.NEUTRAL, Chromatic.FLAT, Chromatic.NEUTRAL]
        self.getDegrees()