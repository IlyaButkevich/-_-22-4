#4.Используя xlwings, добавьте на лист
# Рецепты столбец seconds_formula, показывающий время выполнения рецепта в секундах.
# Выполните задание при помощи формул Excel.
import numpy as np
import pandas as pd
import xlwings as xw
import numpy as np
import xlwings.constants

recipes = pd.read_csv('recipes_sample.csv')
reviews = pd.read_csv('reviews_sample.csv')


wb = xw.Book('Excel_recipes.xlsx')
wb.sheets.add('recipes')
ws = wb.sheets['recipes']
ws.range("A1").value = recipes
ws.range('D:D').insert()
ws['D1'].value = 'seconds_formula'
r1 = 'D2:D' + str(recipes.shape[0])
ws.range(r1).options(expand = 'down').formula = '=E2*60'


#5.Сделайте названия всех добавленных столбцов полужирными и выровняйте по центру ячейки.
ws['D1'].font.bold = True
#ws.range(r1).api.HorizontalAligment = xlwings.constants.HAlign.xlHAlignCenter
#виснет в api


#6.Раскрасьте ячейки столбца minutes в соответствии со следующим правилом: если рецепт выполняется быстрее 5 минут, то цвет - зеленый;
# от 5 до 10 минут - жёлтый; и больше 10 - красный.
a1 = ws['E1'].options(np.array, expand = 'down').value
for i,v in enumerate(a1):
    if i == 0: continue
    elif float(v) >10: col = (255,0,0)
    elif float(v) >5: col = (250,207,105)
    else: col = (0,255,0)
    r2 = 'E' + str(i+1)
    ws.range(r2).color = col

wb.save('recipes01.xlsx')

