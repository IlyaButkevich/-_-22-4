import pandas as pd
import xlwings as xw
import matplotlib.pyplot as plt

# 9. В файле recipes_model.csv находится модель данных предметной области "рецепты".
# При помощи пакета csv считайте эти данные. При помощи пакета xlwings запишите данные
# на лист Модель книги recipes_model.xlsx, начиная с ячейки A2, не используя циклы.
# Сделайте скриншот текущего состояния листа и прикрепите в ячейку ноутбука.
df = pd.read_csv('data/recipes_model.csv', sep='\t', header=None)
print(df.to_string())

wb = xw.Book()
wb.sheets.add('Модель')
ws = wb.sheets['Модель']
ws.range("A2").options(index = False, header = False).value = df
wb.save('recipes_model.xlsx')

# 10. При помощи пакета xlwings добавьте в столбец J формулу для описания столбца на языке SQL. Формула должна реализовывать следующую логику:
# 1. в начале строки идут значения из столбцов В и C (значение столбца С приведено к верхнему регистру), разделенные пробелом
# 2. далее идут слова на основе столбца "Ключ"
#  если в столбце "Ключ" указано значение "PK", то дальше через пробел идет ключевое слово "PRIMARY KEY"
# если в столбце "Ключ" указано значение "FK", то дальше через пробел идет ключевое слово "REFERENCES", затем значения столбцов H и I
# в формате "название_таблицы(название_столбца)"
# 3 если в столбце "Обязательно к заполнению" указано значение "Y" и в столбце "Ключ" указано не "PK", то дальше через пробел идет ключевое слово "NOT NULL".
# Заполните этой формулой необходимое количество строк, используя "протягивание". Количество строк для протягивания определите на основе данных.
# Сделайте скриншот текущего состояния листа и прикрепите в ячейку ноутбука.
column_names=['table', 'param', 'type', 'not null', 'table rus', 'description', 'key', 'key table', 'key param', 'SQL description']
for i in range (10):
    ws[chr(ord('A')+i) + '1'].value = column_names[i]
r1 = 'J2:J' + str(df.shape[0] + 1)
formula = '=CONCATENATE(B2," ", UPPER(C2), IF(G2="PK", " PRIMARY KEY", ""), IF(G2="FK", CONCATENATE(" REFERENCES ", H2, "(", I2, ")"), ""), ' \
          'IF(D2="Y", IF(G2<>"PK", " NOT NULL",""), ""))'
ws.range(r1).options(expand = 'down').formula = formula

# 11. При помощи пакета xlwings измените стилизацию листа Модель.
# для заголовков добавьте заливку цвета 00ccff
# примените автоподбор ширины столбца;
# сделайте шрифт заголовков полужирным;
# добавьте таблице автофильтр.
ws.range('A1:J1').color = '#00ccff'
ws['A1:J1'].font.api.FontStyle = 'полужирный'
ws['A1:J'+  str(df.shape[0]+2)].columns.autofit()
table = ws.tables.add(source=ws['A1'].expand(), name='ModelTable')
table.show_autofilter = True

# 12. Посчитайте количество атрибутов для каждой из сущностей. Создайте лист Статистика и запишите в него результат группировки, начиная с ячейки "А1".
# Визуализируйте полученный результат при помощи столбчатой диаграммы. Сохраните полученную визуализацию на лист Статистика, начиная с ячейки "E2".
# Сделайте скриншот листа Статистика и прикрепите в ячейку ноутбука.

df1 =  df.groupby([0]).agg({1 : ['count']})
print(df1)
wb.sheets.add('Статистика')
ws_stat = wb.sheets['Статистика']
ws_stat.range("A1").options(header = False).value = df1

fig, axes = plt.subplots(nrows = 1, ncols = 1)
df1.plot(ax=axes, kind='bar', legend=False, figsize=(6, 6), xlabel='')
ws_stat.pictures.add(fig, name='MyPlot', update=True, left=ws_stat.range('E2').left, top=ws_stat.range('E2').top)
