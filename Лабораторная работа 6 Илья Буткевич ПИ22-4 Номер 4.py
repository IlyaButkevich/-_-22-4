import re
import pandas as pd

def MultiLine(line,maxlength):
    lines = len(line)//maxlength
    if lines == 0: return line
    for i in range(lines):
        index=(i+1)*maxlength+i
        line = line[:index]+'\n'+line[index:]
    return line

recipes = pd.read_csv('recipes_sample.csv')

recipes =  recipes.dropna(subset=['description'])
recipes = recipes[recipes['description'].str.contains('^this[\w\s]+(,|,\s)but', flags = re.IGNORECASE, regex = True)]
print('Number of needed recipes: ', recipes.shape[0])
recipes = recipes.sample(3)
for i in range(3):
    d = recipes['description'].iloc[i]
    print(MultiLine(d,80),'\n')
