import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from matplotlib import ticker

#Задание номер 3

f_loaded = np.load('average_ratings.npy')
colors = ['r','g','y']
names = ['waffle iron french toast','zwetschgenkuchen bavarian plum cake','lime tea']
x = pd.date_range(start = '1/1/2019', end = '30/12/2021')
fig,axes = plt.subplots(nrows=3, ncols=1)
for i,ax in enumerate(axes):
    p = ax.plot(x, f_loaded[i], color = colors[i], label = names[i])
    ax.xaxis.set_minor_locator(mdates.MonthLocator())
    if i != 2: ax.xaxis.set_major_locator(ticker.NullLocator())
    ax.legend(loc = 'upper left')
    if i == 2: ax.set_xlabel("Дата")
    ax.set_ylabel("Средний рейтинг")
    if i == 0: ax.set_title("Изменение среднего рейтинга трех рецептов")

axes[2].xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.show()
