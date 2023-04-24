import pandas as pd
import time
#Напишите несколько версий функции MAPE (см. MAPE)
# для расчета среднего абсолютного процентного отклонения значения рейтинга отзыва на рецепт
# от среднего значения рейтинга по всем отзывам для этого рецепта.
#Без использования векторизованных операций и методов массивов numpy и без использования numba
#С использованием векторизованных операций и методов массивов numpy, но без использования numba
#Измерьте время выполнения каждой из реализаций.
#Замечание: удалите из выборки отзывы с нулевым рейтингом.

reviews = pd.read_csv('reviews_sample.csv', index_col=0)
reviews =  reviews.dropna(subset=['rating'])
reviews = reviews.loc[reviews['rating'] > 0]

def Mape1(df, rating, recipe_id):
    mape = 0
    n = 0
    for i in range(df.shape[0]):
        if df['recipe_id'].iloc[i] != recipe_id: continue
        r1 = df['rating'].iloc[i]
        f1 = (r1-rating)/r1
        if f1 < 0: f1 = -f1
        mape += f1
        n += 1
    if n: mape = (100.0*mape)/n
    print(mape, n)
    return mape

start = time.time()
Mape1(reviews, 3, 57993)
end = time.time()
print(end-start)

def Mape2(df, rating, recipe_id):
    df1 = df.loc[df['recipe_id']==recipe_id]
    mape = 100*((df1.rating-rating).abs()/df1.rating).mean()
    print(mape)
    return mape

start = time.time()
Mape2(reviews, 3, 57993)
end = time.time()
print(end-start)