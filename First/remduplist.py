# Write a Python function to remove duplicates from a list.

def remListDup(lists):

    dictio = dict([(l, lists.count(l)) for l in lists])
    lists = list(dictio)
    return lists


lista = ['z', 'a', 'a', 'b', 'c']
print(remListDup(lista))
