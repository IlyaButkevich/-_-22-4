import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from matplotlib import ticker

#Задание номер 5

f_loaded = pd.read_csv('recipes_sample.csv')
f_loaded = f_loaded.dropna(subset = ['n_steps'])
df1 = f_loaded.loc[(f_loaded['minutes'] < 5)]
df2 = f_loaded.loc[(f_loaded['minutes'] >= 5) & (f_loaded['minutes'] < 50)]
df3 = f_loaded.loc[(f_loaded['minutes'] >=50)]

fig,axes = plt.subplots(nrows=1, ncols=2)
fig.set_figwidth(10)
row = [0,0,0]
row[0] = df1['n_steps'].mean()
row[1] = df2['n_steps'].mean()
row[2] = df3['n_steps'].mean()
axes[0].bar([0,1,2], row, color = 'r')
axes[0].set_xlabel("Группа рецептов")
axes[0].set_ylabel("Средняя длительность")

row[0] = df1.shape[0]
row[1] = df2.shape[0]
row[2] = df3.shape[0]
axes[1].pie(row, labels = ['Short', 'Middle', 'Long'])
axes[1].set_title('Размеры групп рецептов')
plt.show()
