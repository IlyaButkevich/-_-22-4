import pandas as pd
import scipy
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy import spatial

#3.1
recipes = pd.read_csv('recipes_sample.csv')
recipes =  recipes.dropna(subset=['description'])
recipes = recipes.sample(5)
recipes.reindex()

list1 = []
names = []

vectorizer = TfidfVectorizer()
for index in range(5):
    list1.append(recipes['description'].iloc[index])
    names.append(recipes['name'].iloc[index])
X=vectorizer.fit_transform(list1)
a = X.toarray()

#3.2

df2 = pd.DataFrame(columns=names)
row = [0,0,0,0,0]
for index1 in range(5):
    for index2 in range(5):
        w = spatial.distance.cosine(a[index1], a[index2])
        row[index2] = w
    df2.loc[len(df2)] = row
df2.index = names
print(df2.to_string())

#3.3
#Наиболее похожие - с наименьшими числами, но не 0 (0 это расстояние с самим собой)