import pandas as pd
import nltk
from nltk.corpus import stopwords
from gensim.parsing.preprocessing import remove_stopwords

#2.2

def Calc_Words(df1, n):
    words = {}
    nwords = 0
    for index in range(df1.shape[0]):
        str1 = df1['description'].iloc[index]
        lw = nltk.word_tokenize(str1)
        for item1 in lw:
            if item1.isalpha() == True:
                word = item1.lower()
                nwords+=1
                if word not in words: words[word] = 1
                else: words[word]=words[word]+1

    list1 = list(words.items())
    list1.sort(key = lambda x:x[1], reverse=True)
    del list1[n:]
    return nwords, list1

recipes = pd.read_csv('recipes_sample.csv', nrows=50)
recipes =  recipes.dropna(subset=['description'])
recipes.reindex()
n1, words1 = Calc_Words(recipes, 10)
print(n1)

for index in range(recipes.shape[0]):
    str1 = recipes['description'].iloc[index]
    #str1 = remove_stopwords(str1)
    str1.lower()
    lw = nltk.word_tokenize(str1)
    removed = [word for word in lw if not word in stopwords.words()]
    str1 = ' '.join(removed)
    recipes.at[index, 'description'] = str1


n2, words2 = Calc_Words(recipes, 10)
print(n2)
for i in range(10): print(words1[i], words2[i])

res = (n1 - n2)/n1
print("{:.2f}".format(res))
