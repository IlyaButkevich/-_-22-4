import nltk
import pandas as pd

def PrintSemantic(line):
    lw = nltk.word_tokenize(line)
    tag = nltk.pos_tag(lw)
    for item in tag:
        str1 = "{:^"+str(len(item[0]))+"s}"
        print('',str1.format(item[1]), end='')
    print('')
    for item in tag:
        print('',item[0], end='')
    print('')

recipes = pd.read_csv('recipes_sample.csv')
id = 241106
recipes = recipes.loc[recipes['id'] == id]
name = recipes['name'].iloc[0]

PrintSemantic(name)