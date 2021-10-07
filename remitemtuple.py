#08 Write a Python function to remove an item from a tuple.

def remByPos(tuples, pos = 0):
    lista = list(tuples)

    lista.pop(pos)

    return tuple(lista)

def remByItem(tuples, item):
    lista = list(tuples)

    lista.remove(item)

    return tuple(lista)

tuples = tuple(['a', 'b', '1', 'b', 'c'])

print(remByPos(tuples, 2))

print(remByItem(tuples, 'c'))