import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from matplotlib import ticker
import seaborn as sns

#Задание номер 7


df1 = pd.read_csv('recipes_sample.csv')
df2 = pd.read_csv('reviews_sample.csv')
df1 = df1.dropna(subset = ['n_steps','minutes','n_ingredients'])

df1.rename(columns={'id':'recipe_id'}, inplace=True)
df = df2.merge(df1, on = 'recipe_id')

matrix = df.loc[:,["minutes", "n_steps", "n_ingredients", "rating"]].corr()

fig,axes = plt.subplots(nrows=1, ncols=1)
fig.set_figwidth(8)

sns.heatmap(matrix, ax = axes, annot = True, cmap='YlOrRd')
axes.set_title("Корреляционная матрица числовых столбцов таблиц recipes и reviews")

plt.show()
