# script that pulls the melody from the soprano part, saves the result as a midi file, then generates the resulting note sequence for the magenta model

# USE THE FIRST SYSTEM ARG TO GET FILEPATH OF CHORALE
from music21 import *
import sys

fpath = sys.argv[1]
bwv_num = fpath[fpath.rfind('_')-6:fpath.rfind('_')]

# pull the melody from the chorale
chorale = converter.parse(fpath)
soprano = chorale.parts[0]
soprano.write('midi', fp=fpath[:fpath.rfind('/')+1]+bwv_num+'_Melody.mid')

# create the corresponding note sequence for magenta
note_sequence = []
for n in soprano.recurse().getElementsByClass(note.Note):
    note_sequence.append(n.pitch.midi)
    for i in range(1,int(n.duration.quarterLength*4)):
        note_sequence.append(-2)

note_sequence_str = '[' + ','.join([str(value) for value in note_sequence]) + ']'

with open('./../models/magenta/melodies/'+bwv_num+'.txt', 'w') as f:
    f.write(note_sequence_str)