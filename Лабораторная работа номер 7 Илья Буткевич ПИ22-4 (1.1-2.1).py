import nltk
import pandas as pd
import random

#1.1
recipes = pd.read_csv('recipes_sample.csv')
recipes =  recipes.dropna(subset=['description'])

words = set()
nwords = 0

for index in range(recipes.shape[0]):
    str1 = recipes['description'].iloc[index]
    lw = nltk.word_tokenize(str1)
    for item1 in lw:
        if item1.isalpha() == True:
            words.add(item1.lower())
            nwords+=1

print('Total words:', nwords, 'Unique words:',len(words))

#1.2
rand_i = []
words = list(words)

while len(rand_i) < 10:
    r1 = random.randint(0, len(words) - 1)
    if r1 not in rand_i: rand_i.append(r1)

for i in range(5):
    distance = nltk.edit_distance(words[rand_i[i*2]], words[rand_i[i*2+1]])
    print(words[rand_i[i*2]], words[rand_i[i*2+1]], distance)

#1.3
def Find_words(word, words, k):
    temp_list1 = []
    for item in words:
        temp_list2 = [0,0]
        temp_list2[0] = item
        temp_list2[1] = nltk.edit_distance(word, item)
        temp_list1.append(temp_list2)
    temp_list1.sort(key = lambda x:x[1])
    del temp_list1[k:]
    return temp_list1

a = Find_words('eat', words, 15)
for i in a: print(i)

#2.1
df1 = pd.DataFrame(columns=['word', 'stemmed_word', 'normalized_word'])
df1.set_index('word')

stemmer = nltk.SnowballStemmer('english')
lemmatiser = nltk.WordNetLemmatizer()

for i in words:
    row = [i, stemmer.stem(i),lemmatiser.lemmatize(i)]
    df1.loc[len(df1)] = row
print(df1.head(20))