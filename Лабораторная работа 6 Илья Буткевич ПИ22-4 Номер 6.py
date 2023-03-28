import nltk
import xml.etree.ElementTree as ET

tree = ET.parse('steps_sample.xml')
root = tree.getroot()

unique1 = set()
nwords = 0

for item in root.iter('step'):
    str1 = item.text
    lw = nltk.word_tokenize(str1)
    for item1 in lw:
        if item1.isalpha() == True:
            unique1.add(item1.lower())
            nwords+=1

print('Total words:', nwords, 'Unique words:',len(unique1))