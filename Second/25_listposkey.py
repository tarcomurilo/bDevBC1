#Create a Python function that accepts any number of positional 
# and keyword arguments, and that prints them back to the user. 
# Your output should indicate which values were provided as positional 
# arguments, and which were provided as keyword arguments.

def listPosKeys(*args, **kwargs):
    if args:
        for item in args:
            print(f'Postional argment: {item} ')
    if kwargs:
        for item in kwargs:
            print(f'Keyword argument: {item}')

tupla = (1, 3, 4)
dicta = {
    'b': 'A',
    'B': 2
    }

print('Entering: ', tupla, dicta)

listPosKeys(*tupla, **dicta)