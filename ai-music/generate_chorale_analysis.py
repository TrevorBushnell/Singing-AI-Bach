from music21 import *
import sys

def generate_chord_progressions(score, key_sig):
    # generate the chords
    score_chords = score.chordify()
    score_chords.partName = 'Chords'
    score_chords.id = 'Chords'

    # put the chords in closed position
    for c in score_chords.recurse().getElementsByClass(chord.Chord):
        c.closedPosition(forceOctave=4, inPlace=True)

    # generate the roman numeral analysis for each chord
    for c in score_chords.recurse().getElementsByClass(chord.Chord):
        rn = roman.romanNumeralFromChord(c, key_sig)
        c.addLyric(str(rn.figure))

    score.insert(0, score_chords)


filepath = sys.argv[1]

# read in the score from the filepath
score = converter.parse(filepath)

# try to get the key
key_sig = None
try:
    key_sig = sys.argv[2]
except:
    key_sig = score.analyze('key')

# run the algorithm
generate_chord_progressions(score, key_sig)

# output the result to a pdf file
score.write('musicxml.pdf', fp=filepath[:filepath.find('.', filepath.find('.')+1)]+'.pdf')
