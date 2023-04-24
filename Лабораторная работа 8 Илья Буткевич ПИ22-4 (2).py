from line_profiler import LineProfiler
import pandas as pd
from datetime import datetime
import time

#Какая из созданных функций выполняется медленнее? Что наиболее сильно влияет на скорость выполнения?
# Для ответа использовать профайлер line_profiler.
# Сохраните результаты работы профайлера в отдельную текстовую ячейку и прокомментируйте результаты его работы.
#(*). Сможете ли вы ускорить работу функции 1Б, отказавшись от использования метода iterrows, но не используя метод mean?

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

def C_series():
    start = time.time()
    mean1 = reviews.loc[reviews['date'].dt.year==2010, 'rating'].mean()
    end = time.time()
    print(mean1, 'Время выполнения в секундах C: ', end-start)

def B1():
    start = time.time()
    c1 = 0
    sum1 = 0
    newdf = reviews.loc[reviews['date'].dt.year==2010]
    for index in range(newdf.shape[0]):
        c1 += 1
        sum1 += newdf['rating'].iloc[index]
    mean1 = sum1/c1
    end = time.time()
    print(mean1, 'Время выполнения в секундах B1: ', end-start)
B1()

lp = LineProfiler()
lp_wrapper = lp(A_iterr)
lp_wrapper()
lp.print_stats()

lp = LineProfiler()
lp_wrapper = lp(B_iterr)
lp_wrapper()
lp.print_stats()

lp = LineProfiler()
lp_wrapper = lp(C_series)
lp_wrapper()
lp.print_stats()


"""
Total time: 14.0598 s
Function: A_iterr at line 20

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    20                                           def A_iterr():
    21         1         35.0     35.0      0.0      start = time.time()
    22         1          3.0      3.0      0.0      c1 = 0
    23         1          2.0      2.0      0.0      sum1 = 0
    24    126696  125079692.0    987.2     89.0      for index,row in reviews.iterrows():
    25    114602   14306906.0    124.8     10.2          if row['date'].year != 2010: continue
    26     12094      42111.0      3.5      0.0          c1 += 1
    27     12094    1169311.0     96.7      0.8          sum1 += row['rating']
    28         1          6.0      6.0      0.0      mean1 = sum1/c1
    29         1         20.0     20.0      0.0      end = time.time()
    30         1        326.0    326.0      0.0      print(mean1, 'Время выполнения в секундах A: ', end-start) 
    
    
Total time: 1.36532 s
Function: B_iterr at line 32

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    32                                           def B_iterr():
    33         1         12.0     12.0      0.0      start = time.time()
    34         1          2.0      2.0      0.0      c1 = 0
    35         1          2.0      2.0      0.0      sum1 = 0
    36         1     105369.0 105369.0      0.8      newdf = reviews.loc[reviews['date'].dt.year==2010]
    37     12094   12001905.0    992.4     87.9      for index,row in newdf.iterrows():
    38     12094      39143.0      3.2      0.3          c1 += 1
    39     12094    1506404.0    124.6     11.0          sum1 += row['rating']
    40         1          5.0      5.0      0.0      mean1 = sum1/c1
    41         1         16.0     16.0      0.0      end = time.time()
    42         1        308.0    308.0      0.0      print(mean1, 'Время выполнения в секундах B: ', end-start)
    
Total time: 0.0095753 s
Function: C_series at line 44

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    44                                           def C_series():
    45         1         11.0     11.0      0.0      start = time.time()
    46         1      95435.0  95435.0     99.7      mean1 = reviews.loc[reviews['date'].dt.year==2010, 'rating'].mean()
    47         1         13.0     13.0      0.0      end = time.time()
    48         1        294.0    294.0      0.3      print(mean1, 'Время выполнения в секундах C: ', end-start)
"""

