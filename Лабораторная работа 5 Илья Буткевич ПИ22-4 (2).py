import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

#Задание номер 2

f_loaded = np.load('average_ratings.npy')
colors = ['r','g','y']
names = ['waffle iron french toast','zwetschgenkuchen bavarian plum cake','lime tea']
x = pd.date_range(start = '1/1/2019', end = '30/12/2021')
fig,ax = plt.subplots()
for i in range(3):
    p = plt.plot(x, f_loaded[i], color = colors[i], label = names[i])
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
plt.legend(loc = 'upper left')
plt.xlabel("Дата")
plt.ylabel("Средний рейтинг")
plt.title("Изменение среднего рейтинга трех рецептов")
plt.show()
