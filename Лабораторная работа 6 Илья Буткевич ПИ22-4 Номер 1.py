import pandas as pd
recipes = pd.read_csv('recipes_sample.csv')
df1 = recipes.sample(5)
widths = [10,10]
names = ['id','minutes']

max1 = df1[['id','minutes']].max()
for i in range(2):
    widths[i] = len(str(max1[i]))
    if widths[i] < len(names[i]):
        widths[i] = len(names[i])
    widths[i] += 2


str1 = "|{:^" + str(widths[0]) + "s}|{:^" + str(widths[1]) + "s}|"
print(str1.format(names[0],names[1]))
print('|', end='')
for i in range(widths[0]+widths[1]+1):
    print('-', end='')
print('|')

str2 = "|{:^" + str(widths[0]) + "d}|{:^" + str(widths[1]) + "d}|"
for i in range(5):
    id = df1.iat[i,1]
    minute = df1.iat[i,2]
    print(str2.format(id, minute))
