import xmltodict, json


my_list0 = [
{'part1' : 10, 'part2' : 20, 'part3' :30},
{'part1' : 10, 'part2' : 21, 'part3' :31},
{'part1' : 12, 'part2' : 22, 'part3' :32},
{'part1' : 13, 'part2' : 23, 'part3' :33},
{'part1' : 14, 'part2' : 24, 'part3' :34},
{'part1' : 12, 'part2' : 25, 'part3' :35},
{'part1' : 10, 'part2' : 26, 'part3' :36}
]

print("my_list0 = ",my_list0)

# Question 1

list_cle = []
list_dict = []

for i in my_list0 :
    list_dict.append(i)
    list_cle.append(i['part1'])


my_list1 = [dict(zip([x],[y])) for x,y in zip(list_cle,list_dict)]

print("my_list1 = ", my_list1)

# Question 2
l1 = []
l2 = []
l3 = []
l4 = []
list_cle_2 = [10, 12, 13, 14]

for i in list_dict :
    if i['part1'] == 10 :
        l1.append(i)
    elif i['part1'] == 12 :
        l2.append(i)
    elif i['part1'] == 13 :
        l3.append(i)
    else :
        l4.append(i)

ls = [l1, l2, l3, l4]

my_list2 = [dict(zip([x],[y])) for x,y in zip(list_cle_2,ls)]

print("my_list2 = ", my_list2)

# Question 3

# Question 4

with open("my_list2.xml", "r") as xml_file :      # Lire notre fichier xml,
    data = xmltodict.parse(xml_file.read())       # " data " est la variable dans laquelle nous avons chargé nos données XML après les avoir converties en type de données du dictionnaire.

json_data = json.dumps(data)                     # json_data stocke le ficier json .

with open("my_list2.json", "w") as json_file:
    json_file.write(json_data)
