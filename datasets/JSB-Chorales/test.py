from music21 import *

# List of MIDI pitch values
midi_pitches = [60, 64, 67, 72]  # Replace with your MIDI pitch values

# Create a chord from the MIDI pitch values
my_chord = chord.Chord(midi_pitches)

# Print the chord
print(my_chord.pitchedCommonName)

