import pandas as pd
recipes = pd.read_csv('recipes_sample.csv')
reviews = pd.read_csv('reviews_sample.csv')
#1.Загрузите данные из файлов reviews_sample.csv (ЛР2) и recipes_sample.csv (ЛР5) в виде pd.DataFrame.
# Обратите внимание на корректное считывание столбца(ов) с индексами.
# Оставьте в таблице с рецептами следующие столбцы: id, name, minutes, submitted, description, n_ingredients
a = pd.DataFrame(recipes)
del a['contributor_id']
del a['n_steps']
print(a)

#2.Случайным образом выберите 5% строк из каждой таблицы и сохраните две таблицы на разные листы в один файл recipes.xlsx.
# Дайте листам названия "Рецепты" и "Отзывы", соответствующие содержанию таблиц.
a1 = recipes.sample(frac=0.05)
print(a1)
b1 = reviews.sample(frac=0.05)
print(b1)

import xlwt
import openpyxl
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

with pd.ExcelWriter('recipes.xlsx', engine = 'openpyxl') as writer:
    writer.book = wb
    a1.to_excel(writer, sheet_name = 'recipes')
    b1.to_excel(writer, sheet_name='reviews')
    writer.save()

