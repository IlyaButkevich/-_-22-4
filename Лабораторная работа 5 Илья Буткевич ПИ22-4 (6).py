import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from matplotlib import ticker

#Задание номер 6

f_loaded = pd.read_csv('reviews_sample.csv')
f_loaded['date'] = f_loaded['date'].astype('datetime64[ns]')
df2008 = f_loaded.loc[(f_loaded['date'] >= pd.Timestamp(2008,1,1))&(f_loaded['date'] < pd.Timestamp(2009,1,1))]
df2009 = f_loaded.loc[(f_loaded['date'] >= pd.Timestamp(2009,1,1))&(f_loaded['date'] < pd.Timestamp(2010,1,1))]

fig,axes = plt.subplots(nrows=1, ncols=2)
fig.set_figwidth(10)
df2008.hist(column='rating', ax = axes[0])
df2009.hist(column='rating', ax = axes[1])
axes[0].set_title('Анапа 2008')
axes[1].set_title('Анапа 2009')
fig.suptitle("Гистограммы рейтинга отзывов в 2008 и 2009 годах", fontsize = 14, fontweight = 'bold')
plt.show()
