# import the correct packages
import re
import pandas as pd
from collections import namedtuple

# define a Data datatype to get column and value information
Data = namedtuple('Data', ['col', 'value'])

# read the lines into Python
with open('chorales.lisp', 'r') as f:
    data = f.readlines()

# delete all lines that are just a newline
while '\n' in data:
    data.remove('\n')

# remove the newlines from each row of the data
for i in range(len(data)):
    data[i] = data[i].replace('\n', '')

# create a dictionary mapping each chorale ID to the rows with that chorale
data_dict = {}

for row in data:
    data_dict[int(row[1:row.index(' ')])] = row[row.index(' '):]

# separate out the rows into their own lists
pattern = r'\((.*?)\)' # this is a regular expression to find strings inside ()
for k in data_dict.keys():
    data_dict[k] = data_dict[k].replace('((', '(')
    data_dict[k] = re.findall(pattern, data_dict[k])

# create Data objects for the data
for k in data_dict.keys():
    for i in range(len(data_dict[k])):
        c, v = data_dict[k][i].split()
        data_dict[k][i] = Data(c, int(v))

# print(data_dict[1])
col_names = ['chorale_id', 'st', 'pitch', 'dur', 'keysig', 'timesig', 'fermata']
chorales = []
tmp = []

# now create the csv file
for k in data_dict.keys():
    for val in data_dict[k]:
        if val.col == 'st':
            tmp.append(k)
        
        tmp.append(val.value)

        if val.col == 'fermata':
            chorales.append(tmp)
            tmp = []

t = pd.DataFrame(chorales, columns=col_names)
t.to_csv('chorales_data.csv', index=False)

# get the sum of all rows
sum = 0

for k in data_dict.keys():
    sum += len(data_dict[k])

print(len(t.index))
print(sum)
assert len(t.index) == sum // 6