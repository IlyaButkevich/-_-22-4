import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from matplotlib import ticker
import seaborn as sns

#Задание номер 7
def calc_category(row):
    if row['minutes'] < 5: return 'short'
    if row['minutes'] < 50: return 'middle'
    return 'long'

f_loaded = pd.read_csv('recipes_sample.csv')
f_loaded = f_loaded.dropna(subset = ['n_steps'])

f_loaded['category'] = f_loaded.apply(calc_category, axis = 1)

fig,axes = plt.subplots(nrows=1, ncols=1)
sns.scatterplot(data=f_loaded, x = 'n_steps', y = 'n_ingredients', ax = axes, hue = 'category')
axes.set_title('Диаграмма рассеяния n_steps и n_ingredients')
fig.text(0.1, 0.02, 'зависимость наблюдается', color = 'r')

plt.show()
