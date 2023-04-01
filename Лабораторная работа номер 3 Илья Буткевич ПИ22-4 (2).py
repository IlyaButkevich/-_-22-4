import json
import pickle
import os

#2.1 На основе файла contributors_sample.json создайте словарь следующего вида:
with open ('contributors_sample.json', 'r') as fp:
    dict1 = json.load(fp)
jobs = {}
for item1 in dict1:
    for item2 in item1['jobs']:
        if item2 not in jobs.keys(): jobs[item2] = [item1['username']]
        else: jobs[item2].append(item1['username'])

for k,v in jobs.items():
    print(k, v)

#2.2 Сохраните результаты в файл job_people.pickle и в файл job_people.json с использованием форматов pickle и JSON соответственно.
# Сравните объемы получившихся файлов. При сохранении в JSON укажите аргумент indent.
with open ('test1.json', 'w') as fp:
    json.dump(jobs,fp)
with open ('test1.pickle', 'wb') as fp:
    pickle.dump(jobs,fp)

filestats1 = os.stat('test1.json')
filestats2 = os.stat('test1.pickle')
print('Json size in bytes:', filestats1.st_size, 'Pickle size in bytes:', filestats2.st_size)

#2.3 Считайте файл job_people.pickle и продемонстрируйте, что данные считались корректно.

with open ('test1.pickle', 'rb') as fp:
    jobs1 = pickle.load(fp)
for k,v in jobs1.items():
    print(k, v)