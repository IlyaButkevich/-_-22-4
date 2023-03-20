#3.Используя xlwings, добавьте на лист Рецепты столбец seconds_assign,
# показывающий время выполнения рецепта в секундах. Выполните задание при помощи присваивания массива значений диапазону ячеек.
import numpy as np
import pandas as pd
import xlwings as xw
import numpy as np
recipes = pd.read_csv('recipes_sample.csv')
reviews = pd.read_csv('reviews_sample.csv')


wb = xw.Book('Excel_recipes.xlsx')
wb.sheets.add('recipes')
ws = wb.sheets['recipes']
ws.range("A1").value = recipes
ws.range('D:D').insert()
a1 = ws['E1'].options(np.array, expand = 'down').value
for i,v in enumerate(a1):
    if i == 0:
        a1[0] = 'seconds'
    else:
        b = float(v)*60
        a1[i] = str(b)

ws['D1'].options(transpose = True).value = a1
#list(a1)
wb.save('recipes01.xlsx')





