from music21 import *
import sys

def generate_chord_progressions(score):
    # generate the chords
    score_chords = score.chordify()
    score_chords.partName = 'Chords'
    score_chords.id = 'Chords'

    # put the chords in closed position
    for c in score_chords.recurse().getElementsByClass(chord.Chord):
        c.closedPosition(forceOctave=4, inPlace=True)

    # generate the roman numeral analysis for each chord
    for c in score_chords.recurse().getElementsByClass(chord.Chord):
        if c.beat.is_integer():
            rn = roman.romanNumeralFromChord(c, score.analyze('key'))
            c.addLyric(str(rn.figure))

    score.insert(0, score_chords)


fpath = sys.argv[1]
score = converter.parse(fpath)
generate_chord_progressions(score)
score.write('musicxml.pdf', fp=fpath[:-4]+'.pdf')
