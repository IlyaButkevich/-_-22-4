import json
import columns as columns
import pandas as pd

#1.1 Считайте файл contributors_sample.json. Воспользовавшись модулем json,
# преобразуйте содержимое файла в соответствующие объекты python.
# Выведите на экран информацию о первых 3 пользователях.

with open ('contributors_sample.json', 'r') as fp:
    dict1 = json.load(fp)
for i in range(3):
    print(dict1[i])

#1.2 Выведите уникальные почтовые домены, содержащиеся в почтовых адресах людей

set1 = set()
for item in dict1:
    mail = item['mail'].split('@')
    set1.add(mail[1])
print('\n',set1)

#1.3 Напишите функцию, которая по username ищет человека и выводит информацию о нем.
# Если пользователь с заданным username отсутствует, возбудите исключение ValueError

def Find_user(username, dict1):
    user = [item for item in dict1 if item['username'] == username]
    if len(user) <1: raise ValueError
    for k,v in user[0].items():
        print(k +': ',v)
try:
    Find_user(input("input username: "), dict1)
except ValueError:print('abobus')

#1.4 Посчитайте, сколько мужчин и женщин присутсвует в этом наборе данных.
male = 0
female = 0
for item in dict1:
    if item['sex'] == 'M': male +=1
    else: female +=1
print('Male:',male, 'Female:', female)

#1.5 Создайте pd.DataFrame contributors, имеющий столбцы id, username и sex.
contributors = pd.DataFrame(dict1, columns = ['id','username','sex'])
print(contributors.to_string())

#1.6 Загрузите данные из файла recipes_sample.csv (ЛР2) в таблицу recipes.
# Объедините recipes с таблицей contributors с сохранением строк в том случае,
# если информация о человеке отсутствует в JSON-файле. Для скольких человек информация отсутствует?

recipes = pd.read_csv('recipes_sample.csv')

df1 = pd.merge(left=recipes, right=contributors, left_on='contributor_id', right_on='id', how='left', indicator = True)
df2 = df1[df1['_merge']=='left_only']
missing = df2['contributor_id'].nunique()
print('recipes_n:', str(df1.shape[0]), 'missing people:', missing)
