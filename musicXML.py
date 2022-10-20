HEADER = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 3.1 Partwise//EN" "http://www.musicxml.org/dtds/partwise.dtd">
<score-partwise version="3.1">
  <work>
    <work-title>Sample</work-title>
  </work>
  <defaults>
    <page-layout>
      <page-height>1683.78</page-height>
      <page-width>1190.55</page-width>
      <page-margins type="even">
        <left-margin>56.6929</left-margin>
        <right-margin>56.6929</right-margin>
        <top-margin>56.6929</top-margin>
        <bottom-margin>113.386</bottom-margin>
      </page-margins>
      <page-margins type="odd">
        <left-margin>56.6929</left-margin>
        <right-margin>56.6929</right-margin>
        <top-margin>56.6929</top-margin>
        <bottom-margin>113.386</bottom-margin>
      </page-margins>
    </page-layout>
    <word-font font-family="FreeSerif" font-size="10"/>
    <lyric-font font-family="FreeSerif" font-size="11"/>
  </defaults>
  <credit page="1">
    <credit-words default-x="595.275" default-y="1627.09" justify="center" valign="top" font-size="24">Sample</credit-words>
  </credit>
  <part-list>
    <score-part id="P1">
      <part-name>Piano</part-name>
      <part-abbreviation>Pno.</part-abbreviation>
      <score-instrument id="P1-I1">
        <instrument-name>Piano</instrument-name>
      </score-instrument>
      <midi-device id="P1-I1" port="1"></midi-device>
      <midi-instrument id="P1-I1">
        <midi-channel>1</midi-channel>
        <midi-program>1</midi-program>
        <volume>78.7402</volume>
        <pan>0</pan>
      </midi-instrument>
    </score-part>
  </part-list>
  <part id="P1">
"""

FIRST_MEASURE1 = """      <print>
        <system-layout>
          <system-margins>
            <left-margin>21.00</left-margin>
            <right-margin>695.27</right-margin>
          </system-margins>
          <top-system-distance>170.00</top-system-distance>
        </system-layout>
        <staff-layout number="2">
          <staff-distance>65.00</staff-distance>
        </staff-layout>
      </print>
      <attributes>
        <divisions>1</divisions>
        <key>\n"""

FIRST_MEASURE2 = """        </key>
        <time>
          <beats>4</beats>
          <beat-type>4</beat-type>
        </time>
        <staves>2</staves>
        <clef number="1">
          <sign>G</sign>
          <line>2</line>
        </clef>
        <clef number="2">
          <sign>F</sign>
          <line>4</line>
        </clef>
      </attributes>
"""

FOOTER = "  </part>\n</score-partwise>\n"
BACKUP = "      <backup>\n        <duration>4</duration>\n      </backup>\n"


class MusicXML:
    def __init__(self, metrumBeams):
        self.width = 300
        self.metrumBeams = metrumBeams
        self.stem = ["down", "up"]
        self.voice = [6, 5, 2, 1]
        self.noteType = ["quarter", "half"]
        self.output = ""

    def firstMeasureConfig(self, key):
        configStr = FIRST_MEASURE1
        configStr += "<fifths>" + str(key.getFifths()) + "</fifths>\n"
        configStr += FIRST_MEASURE2
        return configStr

    def getMeasureString(self, measureNumber: int):
        return "    <measure number=\"" + str(measureNumber) + "\" width=\"" + str(self.width) + "\">\n"

    def pause(self, voice, duration):
        pauseStr = "      <note>\n        <rest/>\n"
        pauseStr += "        <duration>" + str(duration) + "</duration>\n"
        pauseStr += "        <voice>" + str(voice) + "</voice>\n"
        pauseStr += "        <type>" + self.noteType[duration - 1] + "</type>\n"
        pauseStr += "        <staff>" + str(voice // 4 + 1) + "</staff>\n      </note>\n"
        return pauseStr

    def export(self, key, chords: list):
        measureNumber = 1
        measureStrings = []
        noteStrings = []
        measureString = self.getMeasureString(measureNumber) + self.firstMeasureConfig(key)
        for i in range(len(chords)):
            chord = chords[i]
            for j in range(4):
                note = chord[j]
                noteString = "      <note>\n"
                noteString += "        <pitch>\n"
                noteString += "          <step>" + note.degree.code() + "</step>\n"
                if note.chromatic != 0: noteString += "          <alter>" + str(note.chromatic) + "</alter>\n"
                noteString += "          <octave>" + str(note.octave) + "</octave>\n"
                noteString += "        </pitch>\n"
                noteString += "        <duration>1</duration>\n"
                noteString += "        <voice>" + str(self.voice[j]) + "</voice>\n"
                noteString += "        <type>quarter</type>\n"
                noteString += "        <stem>" + str(self.stem[j % 2]) + "</stem>\n"
                noteString += "        <staff>" + str((5 - j) // 2) + "</staff>\n"
                noteString += "      </note>\n"
                noteStrings.append(noteString)
            if i % self.metrumBeams == 3 or i == len(chords) - 1:
                for j in range(4):
                    for k in range(len(noteStrings)):
                        if k % 4 == j: measureString += noteStrings[k]
                    if len(noteStrings) // 4 % 2 == 1: measureString += self.pause(self.voice[j], 1)
                    if len(noteStrings) // 4 <= 2:     measureString += self.pause(self.voice[j], 2)
                    measureString += BACKUP

                measureString += "    </measure>\n"
                measureStrings.append(measureString)
                measureNumber += 1
                measureString = self.getMeasureString(measureNumber)
                noteStrings = []

        self.output = HEADER + "".join(measureStrings) + FOOTER
        self.save()

    def save(self):
        with open('sample.musicxml', 'w', encoding="utf-8") as file:
            file.write(self.output)
