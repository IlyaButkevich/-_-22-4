import nltk
import pandas as pd

def Ultramegacount(row):
    return len(nltk.sent_tokenize(row['description']))

recipes = pd.read_csv('recipes_sample.csv')
recipes =  recipes.dropna(subset=['description'])
recipes['n_sentences'] = recipes.apply(Ultramegacount, axis=1)

recipes = recipes.sort_values('n_sentences', ascending=False)
cols = recipes.columns.tolist()
cols = cols[-1:] + cols[:-1]
recipes = recipes[cols]
recipes =  recipes.head(5)
print(recipes.to_string())

