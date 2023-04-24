import random
import pandas as pd
import numpy as np
import string
#1.Сгенерируйте массив A из N=1млн случайных целых чисел на отрезке от 0 до 1000. Пусть B[i] = A[i] + 100.
# Посчитайте среднее значение массива B.

list1 = []
list2 = []
sum1 = 0

for i in range(1000000):
    list1.append(random.randint(0, 1000))

for i in range(len(list1)):
    list2.append(list1[i]+100)
    sum1+=list2[i]

mean1 = sum1/len(list2)
print(mean1)


#2.Создайте таблицу 2млн строк и с 4 столбцами, заполненными случайными числами.
# Добавьте столбец key, которые содержит элементы из множества английских букв.
# Выберите из таблицы подмножество строк, для которых в столбце key указаны первые 5 английских букв.

df1 = pd.DataFrame(np.random.rand(2000000, 4))
df1['key'] = [''.join(random.choice(string.ascii_letters) for x in range(10)) for _ in df1.index]
df1 = df1[df1['key'].str.contains('a', case = False, regex = False)&
df1['key'].str.contains('b', case = False, regex = False)&
df1['key'].str.contains('c', case = False, regex = False)&
df1['key'].str.contains('d', case = False, regex = False)&
df1['key'].str.contains('e', case = False, regex = False)]
print(df1.to_string())
