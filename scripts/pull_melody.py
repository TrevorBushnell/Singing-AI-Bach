# this code cell tries to pull the soprano part from a chorale and save the output as musicxml
from music21 import *
import sys

chorale20 = converter.parse(sys.argv[1])


s = stream.Score()
s.insert(0, chorale20.parts[0])
s.write('midi', fp='/home/tbushnell/GitHub/Singing-AI-Bach/scripts/output.mid')