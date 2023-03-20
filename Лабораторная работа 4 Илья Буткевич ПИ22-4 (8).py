#8.Напишите функцию validate(), которая проверяет соответствие всех строк из листа Отзывы следующим правилам:
#Рейтинг - это число от 0 до 5 включительно
#Соответствующий рецепт имеется на листе Рецепты
#В случае несоответствия этим правилам, выделите строку красным цветом
import numpy as np
import pandas as pd
import xlwings as xw
import numpy as np
recipes = pd.read_csv('recipes_sample.csv')
reviews = pd.read_csv('reviews_sample.csv')

#reviews = reviews.sample(50)
#recipes = recipes.sample(50)

wb = xw.Book('Excel_recipes.xlsx')
wb.sheets.add('recipes')
wb.sheets.add('reviews')
ws = wb.sheets['recipes']
ws2 = wb.sheets['reviews']
ws.range("A1").value = recipes
ws2.range("A2").value = reviews

def validate():
    temp = 0
    for i,row in reviews.iterrows():
        if i <=2: continue
        temp += 1
        if temp>10: break
        v = row[4] #rating
        flag1 = 0
        if float(v) > 5 or float(v) < 0: flag1 = 1
        else:
            df1 = recipes.loc[(recipes['id'] == row[2])]
            if df1.shape[0] <1: flag1 = 1
        r2 = 'A' + str(i) + ':G' + str(i)
        if flag1 == 1:
            ws2.range(r2).color = (255,0,0)






validate()
