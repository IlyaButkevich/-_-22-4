import pandas as pd
import xml.etree.ElementTree as ET

def Get_Steps_by_id(recipe_id):
    list1 = []
    text = ".//recipe/[id ='" + str(recipe_id) + "']"
    a = root.findall(text)
    for steps in a[0].iter('step'):
        list1.append(steps.text)
    return list1

def Showinfo(name, minutes, contributor_id, steps):
    res1 = name + '\n\n'
    maxlen = 0
    for i,step in enumerate(steps):
        res1 += str(i+1) + '. ' + step + '\n'
        if len(step) > maxlen:
            maxlen = len(step)
    for i in range(maxlen+4): res1 += '-'
    res1 += '\nАвтор: ' + str(contributor_id) + '\n'
    res1 += 'Среднее время приготовления: ' + str(minutes) + ' минут'
    return res1


recipes = pd.read_csv('recipes_sample.csv')
tree = ET.parse('steps_sample.xml')
root = tree.getroot()
id = 170895
df1 = recipes.loc[recipes['id']==id]
name = df1['name'].iloc[0]
minutes = df1['minutes'].iloc[0]
contributor_id = df1['contributor_id'].iloc[0]
steps = Get_Steps_by_id(id)

print(Showinfo(name, minutes, contributor_id, steps))
