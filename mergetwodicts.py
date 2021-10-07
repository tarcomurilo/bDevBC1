#09 Write a Python function to merge two dictionaries.

def mergeTwoDicts(dict1, dict2):
    dict3 = {}
    for item in dict1:
        dict3[item] = dict1[item]
    for item in dict2:
        dict3[item] = dict2[item]

    return dict3

dict1 = {"a": 1, "b": "c", "8": "4"}
dict2 = {"z": 2, "y": "x", "4": "3"}

print(mergeTwoDicts(dict1, dict2))