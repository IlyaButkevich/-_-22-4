import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from matplotlib import ticker

#Задание номер 4

f_loaded = np.load('visitors.npy')
fig,axes = plt.subplots(nrows=1, ncols=2)
fig.set_figwidth(10)
for i,ax in enumerate(axes):
    ax.plot(f_loaded)
    if i == 1: ax.set_yscale('log')
    ax.set_xlabel("Количество дней с момента акции")
    ax.set_ylabel("Число посетителей")
    ax.set_title("$y(x)=λe^{-λx}$")
    ax.plot([0,100],[100, 100], color = 'r')
    ax.text(30,105, 'y(x) = 100', fontsize = 12, color = 'r')
fig.suptitle("Изменение количества пользователей в линейном и логарифмическом масштабе", fontsize = 14, fontweight = 'bold')
plt.show()
