import json
import pandas as pd
from music21 import *

# read the JSON data
with open('Jsb16thSeparated.json', 'r') as f:
    json_data = json.load(f)

data_list = []
chorale_idx = 0

# parse the JSON data
for k in json_data.keys():
    data = []
    for chorale in json_data[k]:
        chorale_idx += 1
        timestep_idx = 0
        
        for timestep in chorale:
            timestep_idx += 1
            row = []
            row.append(chorale_idx)
            row.append(timestep_idx)

            for note in timestep:
                row.append(note)

            data.append(row)

    curr_df = pd.DataFrame(data, columns=['ChoraleID', 'TimestepID', 'SopranoMidi', 'AltoMidi', 'TenorMidi', 'BassMidi'])
    curr_df.to_csv(f'JSB-Chorales-{k}.csv', index=False)
    data_list.append(curr_df)
    
df = pd.concat(data_list, ignore_index=True)

# convert MIDI values to notes
voices = {'Soprano':[], 'Alto':[], 'Tenor':[], 'Bass':[]}

for i in df.index:
    for voice in voices.keys():
        curr_note = pitch.Pitch(midi=df[f'{voice}Midi'][i])
        voices[voice].append(f'{curr_note.name}{curr_note.octave}')

for voice in voices.keys():
    df[voice] = voices[voice]

df = df.reindex(columns=['ChoraleID', 'TimestepID', 'Soprano', 'SopranoMidi', 'Alto', 'AltoMidi', 'Tenor', 'TenorMidi', 'Bass', 'BassMidi'])

# generate chords in a separate column
chords = []
for i in df.index:
    chords.append(chord.Chord(f"{df['Soprano'][i]} {df['Alto'][i]} {df['Tenor'][i]} {df['Bass'][i]}").pitchedCommonName)

df['Chord'] = chords

# write the data to a csv file
df.to_csv('JSB-Chorales.csv', index=False)
