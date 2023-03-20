import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Задание номер 1
f_loaded = np.load('average_ratings.npy')
colors = ['r','g','y']
names = ['waffle iron french toast','zwetschgenkuchen bavarian plum cake','lime tea']
for i in range(3):
    p = plt.plot(f_loaded[i], color = colors[i], label = names[i])
plt.legend(loc = 'upper left')
plt.xlabel("Номер дня")
plt.ylabel("Средний рейтинг")
plt.title("Изменение среднего рейтинга трех рецептов")
plt.show()

