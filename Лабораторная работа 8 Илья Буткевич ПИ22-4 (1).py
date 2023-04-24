import pandas as pd
from datetime import datetime
import time

#1. В файлах recipes_sample.csv и reviews_sample.csv (ЛР 2) находится информация об рецептах блюд и отзывах на эти рецепты соответственно.
# Загрузите данные из файлов в виде pd.DataFrame с названиями recipes и reviews.
# Обратите внимание на корректное считывание столбца(ов) с индексами. Приведите столбцы к нужным типам.
#Реализуйте несколько вариантов функции подсчета среднего значения столбца rating из таблицы reviews для отзывов, оставленных в 2010 году.
#A. С использованием метода DataFrame.iterrows исходной таблицы;
#Б. С использованием метода DataFrame.iterrows таблицы, в которой сохранены только отзывы за 2010 год;
#В. С использованием метода Series.mean.
#Проверьте, что результаты работы всех написанных функций корректны и совпадают. Измерьте выполнения всех написанных функций.

recipes = pd.read_csv('recipes_sample.csv')
reviews = pd.read_csv('reviews_sample.csv', index_col=0)

recipes['name'] = recipes['name'].astype("string")
recipes['description'] = recipes['description'].astype("string")
recipes['submitted'] = recipes['submitted'].astype("datetime64[ns]")
reviews['review'] = reviews['review'].astype("string")
reviews['date'] = reviews['date'].astype("datetime64[ns]")

def A_iterr():
    start = time.time()
    c1 = 0
    sum1 = 0
    for index,row in reviews.iterrows():
        if row['date'].year != 2010: continue
        c1 += 1
        sum1 += row['rating']
    mean1 = sum1/c1
    end = time.time()
    print(mean1, 'Время выполнения в секундах A: ', end-start)
A_iterr()

def B_iterr():
    start = time.time()
    c1 = 0
    sum1 = 0
    newdf = reviews.loc[reviews['date'].dt.year==2010]
    for index,row in newdf.iterrows():
        c1 += 1
        sum1 += row['rating']
    mean1 = sum1/c1
    end = time.time()
    print(mean1, 'Время выполнения в секундах B: ', end-start)
B_iterr()

def C_series():
    start = time.time()
    mean1 = reviews.loc[reviews['date'].dt.year==2010, 'rating'].mean()
    end = time.time()
    print(mean1, 'Время выполнения в секундах C: ', end-start)
C_series()



