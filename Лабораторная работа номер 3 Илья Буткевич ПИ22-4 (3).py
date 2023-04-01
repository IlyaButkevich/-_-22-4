import xml.etree.ElementTree as ET
import json
import pandas as  pd

#3.1 По данным файла steps_sample.xml
# сформируйте словарь с шагами по каждому рецепту вида {id_рецепта: ["шаг1", "шаг2"]}.
# Сохраните этот словарь в файл steps_sample.json

#3.2 По данным файла steps_sample.xml сформируйте словарь следующего вида: кол-во_шагов_в_рецепте: [список_id_рецептов]

#3.3 Получите список рецептов, в этапах выполнения которых есть информация о времени (часы или минуты).
# Для отбора подходящих рецептов обратите внимание на атрибуты соответствующих тэгов.

tree = ET.parse('steps_sample.xml')
root = tree.getroot()
a = root.findall('.//recipe/')

dict1 = {}
dict2 = {}
idtimeset = set()
timelist = ['has_minutes', 'has_hours']

for i in range(len(a)):
    if a[i].tag == 'id':
        id1 = int(a[i].text)
    else:
        templist = []
        for i1 in a[i].iter('step'):
            templist.append(i1.text)
            if id1 not in idtimeset:
                if any(item in i1.attrib.keys() for item in timelist):
                    idtimeset.add(id1)
        dict1[id1] = templist
        stepsn = len(templist)
        if stepsn not in dict2.keys():
            dict2[stepsn] = [id1]
        else: dict2[stepsn].append(id1)
with open ('steps_sample.json', 'w') as fp:
    json.dump(dict1,fp)

idtimelist = list(idtimeset)
print('idtime_n:', str(len(idtimelist)))
print(len(dict1))
for k,v in dict2.items():
    print(k,v)

#3.4 Загрузите данные из файла recipes_sample.csv (ЛР2) в таблицу recipes. Для строк, которые содержат пропуски в столбце n_steps,
# заполните этот столбец на основе файла steps_sample.xml. Строки, в которых столбец n_steps заполнен, оставьте без изменений.

recipes = pd.read_csv('recipes_sample.csv')
for i in range(recipes.shape[0]):
    if pd.isna(recipes['n_steps'].iloc[i]==False): continue
    id = recipes['id'].iloc[i]
    n_steps = len(dict1[id])
    recipes.at[i, 'n_steps'] = n_steps

print(recipes.head(10).to_string())

#3.5 Проверьте, содержит ли столбец n_steps пропуски.
# Если нет, то преобразуйте его к целочисленному типу и сохраните результаты в файл recipes_sample_with_filled_nsteps.csv

if recipes['n_steps'].isnull().values.any() == False:
    recipes['n_steps'] = recipes['n_steps'].astype('int')
recipes.to_csv('recipes_sample_with_filled_nsteps.csv', index = False)