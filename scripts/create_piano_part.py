from music21 import *
import sys

score = converter.parse(sys.argv[1])

# Create treble and bass parts
treble_part = stream.Part()
bass_part = stream.Part()
chords = score.chordify()

for c in chords.recurse().getElementsByClass(chord.Chord):
    # Extract the pitches from the chord
    pitches = c.pitches

    # Create notes for treble and bass
    treble_notes = [note.Note(p) for p in pitches[2:]]  # Higher two notes on treble clef
    bass_notes = [note.Note(p) for p in pitches[:2]]  # Lower two notes on bass clef

    # Create treble and bass chords
    treble_chord = chord.Chord(treble_notes)
    bass_chord = chord.Chord(bass_notes)

    # Append chords to respective parts
    treble_part.append(treble_chord)
    bass_part.append(bass_chord)

# Create piano score with treble and bass parts
piano_reduction = stream.Score()
piano_reduction.insert(0, treble_part)
piano_reduction.insert(0, bass_part)
piano_reduction.show()

new_score = stream.Score()
new_score.append(score)
new_score.append(piano_reduction)
new_score.show()