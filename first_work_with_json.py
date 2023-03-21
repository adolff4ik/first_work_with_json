import json
import os

list_one = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0,]

dict_one = {
    'player': '',
    'game': '',
    'wins': '',
}

with open(os.path.join('Desktop','Новая папка','data.json'), 'r', encoding='utf_8') as f:
    text = json.load(f)
print(text[0])

i = 0

w = 0

for a in range(len(text)):
    for q in dict_one.keys():
       print(q + ':', text[w][i])
       i += 1
       if i == 3:
        i = 0
    w += 1

#print(os.getcwd())

#dict_one['player']='Melisa'

#dict_one.setdefault(list_one[i], list_two[i])

#print(dict_one.keys())
