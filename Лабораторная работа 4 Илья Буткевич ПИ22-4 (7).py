#7.Добавьте на лист Рецепты столбец n_reviews, содержащий кол-во отзывов для этого рецепта.
# Выполните задание при помощи формул Excel.
import numpy as np
import pandas as pd
import xlwings as xw
import numpy as np
recipes = pd.read_csv('recipes_sample.csv')
reviews = pd.read_csv('reviews_sample.csv')

#recipes = recipes.sample(50)
#reviews = reviews.sample(50)

wb = xw.Book('Excel_recipes.xlsx')
wb.sheets.add('recipes')
wb.sheets.add('reviews')
ws = wb.sheets['recipes']
ws2 = wb.sheets['reviews']
ws.range("A1").value = recipes
ws2.range("A2").value = reviews
ws.range('D:D').insert()
ws['D1'].value = 'n_reviews'
#r1 = "=СЧЁТЕСЛИ('reviews'!D2:D" + str(reviews.shape[0]) + ";'recipes'!C2)"
r1 = "=COUNTIF('reviews'!D2:D" + str(reviews.shape[0]) + ",'recipes'!C2)"
r2 = 'D2:D' + str(recipes.shape[0])
ws.range(r2).options(expand = 'down').value = r1






wb.save('N_7.xlsx')