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
steps = Get_Steps_by_id(72367)

for i in steps:
    str1 = re.sub(" / ","/", i)
    print(str1)