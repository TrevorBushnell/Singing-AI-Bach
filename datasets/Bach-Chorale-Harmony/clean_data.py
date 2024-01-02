import pandas as pd

# read the data
df = pd.read_csv('jsbach_chorals_harmony.csv')

cols = [c for c in df.columns if c not in ['ChoraleID', 'EventNum', 'Bass', 'Meter', 'Chord']]

for c in cols:
    df[c] = df[c].map({'YES':True, 'NO':False})

df.to_csv('Bach-Chorale-Harmony.csv', index=False)