import random

from harmonicSlice import HarmonicSlice
from voiceBounds import VoiceBounds
from key import Key

from tonic import Tonic
from subdominant import Subdominant
from mollS import MollS
from s6 import S6
from dominant import Dominant
from d64 import D64
from d7 import D7
from d7not1 import D7not1
from d7not5 import D7not5
from dch import Dch
from d9 import D9
from d9not1 import D9not1
from sII import SII
from sN import SN
from mollDVII import MollDVII
from tIII import TIII
from dIII import DIII
from tVI import TVI
from mollTVIobn import MollTVIobn
from sVI import SVI

from musicXML import MusicXML


class Parser:
    def __init__(self):
        self.harmonicSlices = []
        self.chords = []
        self.metrumBeams = 0
        self.key = None

    def getSlices(self, functions: list, key: Key, voiceBounds: VoiceBounds, metrumList: list):
        self.key = key
        self.metrumBeams = len(metrumList)
        i = 0
        for function in functions:
            metrum = metrumList[i]
            function = function.split("$")
            ingredientBounds = function[1:]
            function = function[0]

            match function:
                case "T":           harmonicSlice = HarmonicSlice(key, voiceBounds, Tonic(), metrum)
                case "S":           harmonicSlice = HarmonicSlice(key, voiceBounds, Subdominant(), metrum)
                case "S6":          harmonicSlice = HarmonicSlice(key, voiceBounds, S6(), metrum)
                case "mollS":       harmonicSlice = HarmonicSlice(key, voiceBounds, MollS(), metrum)
                case "D":           harmonicSlice = HarmonicSlice(key, voiceBounds, Dominant(), metrum)
                case "D64":         harmonicSlice = HarmonicSlice(key, voiceBounds, D64(), metrum)
                case "D7":          harmonicSlice = HarmonicSlice(key, voiceBounds, D7(), metrum)
                case "D7n1":        harmonicSlice = HarmonicSlice(key, voiceBounds, D7not1(), metrum)
                case "D7n5":        harmonicSlice = HarmonicSlice(key, voiceBounds, D7not5(), metrum)
                case "Dch":         harmonicSlice = HarmonicSlice(key, voiceBounds, Dch(), metrum)
                case "D9":          harmonicSlice = HarmonicSlice(key, voiceBounds, D9(), metrum)
                case "D9n1":        harmonicSlice = HarmonicSlice(key, voiceBounds, D9not1(), metrum)
                case "SII":         harmonicSlice = HarmonicSlice(key, voiceBounds, SII(), metrum)
                case "SN":          harmonicSlice = HarmonicSlice(key, voiceBounds, SN(), metrum)
                case "mollDVII":    harmonicSlice = HarmonicSlice(key, voiceBounds, MollDVII(), metrum)
                case "DIII":        harmonicSlice = HarmonicSlice(key, voiceBounds, DIII(), metrum)
                case "TIII":        harmonicSlice = HarmonicSlice(key, voiceBounds, TIII(), metrum)
                case "TVI":         harmonicSlice = HarmonicSlice(key, voiceBounds, TVI(), metrum)
                case "mollTVIobn":  harmonicSlice = HarmonicSlice(key, voiceBounds, MollTVIobn(), metrum)
                case "SVI":         harmonicSlice = HarmonicSlice(key, voiceBounds, SVI(), metrum)
                case _:             raise Exception("function not found")

            if harmonicSlice.harmonicFunction.bassBound != 0:
                harmonicSlice.bassBound = harmonicSlice.harmonicFunction.bassBound
            if harmonicSlice.harmonicFunction.sopranBound != 0:
                harmonicSlice.sopranBound = harmonicSlice.harmonicFunction.sopranBound

            for ib in ingredientBounds:
                if ib[0] == 'd':
                    if harmonicSlice.harmonicFunction.bassBound == 0: harmonicSlice.bassBound = int(ib[1:])
                    else: raise Exception(function, "function has already bass bound")
                if ib[0] == 'u':
                    if harmonicSlice.harmonicFunction.sopranBound == 0: harmonicSlice.sopranBound = int(ib[1:])
                    else: raise Exception(function, "function has already sopran bound")
            self.harmonicSlices.append(harmonicSlice)
            i = (i + 1) % 4

        self.harmonicSlices[0].isFirst = True
        self.harmonicSlices[0].bassBound = 1
        self.harmonicSlices[len(self.harmonicSlices)-1].isLast = True
        self.harmonicSlices[len(self.harmonicSlices)-1].bassBound = 1

        self.harmonicSlices[0].harmonize()
        for i in range(1, len(self.harmonicSlices)):
            self.harmonicSlices[i].harmonize(self.harmonicSlices[i-1])

    def printSlices(self):
        for hSlice in self.harmonicSlices:
            hSlice.print()
            print("----------------------------")

    def getOutput(self, seed = 0):
        ends = []
        visited = {}
        length = {}
        previous = {}
        q = []
        currentSlice = self.harmonicSlices[len(self.harmonicSlices)-1].mainSlice
        for chord in currentSlice.body:
            q.append((currentSlice, chord))
            visited[(currentSlice, chord)] = True
            length[(currentSlice, chord)] = 0

        while q:
            currentSlice, chord = q.pop(0)
            if not currentSlice.body[chord]: ends.append((currentSlice, chord))
            for vertex in currentSlice.body[chord]:
                if vertex not in visited:
                    q.append(vertex)
                    visited[vertex] = True
                    length[vertex] = length[(currentSlice, chord)] + 1
                    previous[vertex] = (currentSlice, chord)

        # arbitrary choice
        if len(ends) == 0:
            print("No solution founded")
            return
        random.seed(seed)
        vertex = ends[random.randrange(len(ends))]
        for end in ends:
            if length[end] < length[vertex]: vertex = end
        path = [vertex]
        while vertex in previous:
            path.append(previous[vertex])
            vertex = previous[vertex]

        for p in path: self.chords.append(p[1])

    def printOutput(self):
        for chord in self.chords: print(chord)

    def export(self):
        musicXML = MusicXML(self.metrumBeams)
        musicXML.export(self.key, self.chords)
