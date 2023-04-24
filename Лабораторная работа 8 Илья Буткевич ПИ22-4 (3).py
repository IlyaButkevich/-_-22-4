from line_profiler import LineProfiler
import time
import pandas as pd
reviews = pd.read_csv('reviews_sample.csv', index_col=0, nrows=20000)
reviews['review'] = reviews['review'].astype("string")
reviews['date'] = reviews['date'].astype("datetime64[ns]")

def get_word_reviews_count(df):
    start = time.time()
    word_reviews = {}
    for _, row in df.dropna(subset=['review']).iterrows():
        recipe_id, review = row['recipe_id'], row['review']
        words = review.split(' ')
        for word in words:
            if word not in word_reviews:
                word_reviews[word] = []
            word_reviews[word].append(recipe_id)
    
    word_reviews_count = {}
    for _, row in df.dropna(subset=['review']).iterrows():
        review = row['review']
        words = review.split(' ')
        for word in words:
            word_reviews_count[word] = len(word_reviews[word])
    end = time.time()
    print('Время выполнения в секундах: ', end - start)
    #print(word_reviews_count)

def get_word_reviews_count2(df):
    start = time.time()
    word_reviews_count = {}
    df = df.dropna(subset=['review'])
    for index in  range(df.shape[0]):
        review = df['review'].iloc[index]
        words = review.split(' ')
        for word in words:
            if word not in word_reviews_count.keys():
                word_reviews_count[word] = 1
            else: word_reviews_count[word] = word_reviews_count[word] + 1
    end = time.time()
    print('Время выполнения в секундах: ', end - start)
    #print(word_reviews_count)

get_word_reviews_count(reviews)
get_word_reviews_count2(reviews)