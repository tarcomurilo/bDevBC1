#Create a Python function that accepts any number of numbers as 
#positional arguments and prints the sum of those numbers.

def sumPositional(*args):
    result = 0

    for item in args:
        for arg in item:
            result = result + arg
    
    return result

tupla = (1, 3, 4)
lista2 = [100, 200]

print('Entering: ',tupla, lista2)
print('Result: ', sumPositional(tupla, lista2))