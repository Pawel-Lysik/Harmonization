import sys

from chromatic import Chromatic
from mode import Mode
from sound import Sound
from key import Key
from pitch import Pitch
from voiceBound import VoiceBound
from voiceBounds import VoiceBounds
from metrum import Metrum
from parserModule import Parser

bassBound = VoiceBound(Pitch(2, Sound.E), Pitch(4, Sound.E))
tenorBound = VoiceBound(Pitch(3, Sound.C), Pitch(4, Sound.G))
altBound = VoiceBound(Pitch(3, Sound.G), Pitch(5, Sound.D))
sopranoBound = VoiceBound(Pitch(4, Sound.C), Pitch(6, Sound.C))
voiceBounds = VoiceBounds(bassBound, tenorBound, altBound, sopranoBound)

metrum = [Metrum.FIRST, Metrum.WEAK, Metrum.STRONG, Metrum.END]
mainKey = Key(Sound.C, Mode.DUR, Chromatic.NEUTRAL)

parser = Parser()
perfectCadence = ["T", "S$d1", "D$d1", "T"]
characteristicFunctionsCadence = ["T$u5", "T$d3", "S", "S6", "D64", "D", "D7", "D9", "T"]
auxDegreesCadence = ["T", "TIII", "S", "SII", "D", "DIII", "D7", "Dch", "TVI", "S", "D64", "D", "T"]
mollChordsCadence = ["T", "mollS", "D", "D7", "mollTVIobn", "SN", "D", "T"]
incompleteChordsCadence = ["T", "S", "D7n5", "D7n1", "T", "S6", "D9", "D9n1", "T"]
cadencesMap = {
    "perfectCadence": perfectCadence,
    "characteristicFunctionsCadence": characteristicFunctionsCadence,
    "auxDegreesCadence": auxDegreesCadence,
    "mollChordsCadence": mollChordsCadence,
    "incompleteChordsCadence": incompleteChordsCadence
}
seed = 3
if len(sys.argv) == 2: seed = int(sys.argv[1])
inputStr = input("Enter a harmonic sequence or cadence name:")
if inputStr in cadencesMap: functions = cadencesMap[inputStr]
else: functions = inputStr.split()
parser.getSlices(functions, mainKey, voiceBounds, metrum)
parser.getOutput(3)  # optional seed
parser.printOutput()
parser.export()
