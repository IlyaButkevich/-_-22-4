import re
import xml.etree.ElementTree as ET

def Get_Steps_by_id(recipe_id):
    list1 = []
    text = ".//recipe/[id ='" + str(recipe_id) + "']"
    a = root.findall(text)
    for steps in a[0].iter('step'):
        list1.append(steps.text)
    return list1

tree = ET.parse('steps_sample.xml')
root = tree.getroot()
steps = Get_Steps_by_id(25082)

for i in steps:
    match = re.search(r'\d+\s(hour|hours|minute|minutes)',i)
    if match: print(match[0])