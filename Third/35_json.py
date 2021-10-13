#Write a Python program that reads a JSON object from a file, 
#sorts the object keys in ascending order,
#then writes the JSON object back into the file.

import json

with open("c:\\Users\\Tarco.Oliveira\\Documents\\GitHub\\bDevBC1\\Third\\35_json.json", "r") as jsonfile:
    data = json.load(jsonfile)

lista = list(data)

lista.sort()

newDict = {}
for item in lista:
    newDict[item] = data[item]

print(newDict)

with open("c:\\Users\\Tarco.Oliveira\\Documents\\GitHub\\bDevBC1\\Third\\35_json.json", "w") as jsonfile:
    json.dump(newDict, jsonfile)