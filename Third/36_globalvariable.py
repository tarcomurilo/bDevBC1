#Write a python file with two functions: 
# a function that receives a number and appends to a global variable list,
# and another function that returns this list ordered.

global_variable = []

def appendGlobal(number):
    try:
        global_variable.append(int(number))
    except:
        global_variable.append(float(number))
    finally:
        pass

def sortGlobal(globVar=global_variable):
    globVar.sort()
    return globVar

flag = True

while flag:
    number = input('Add Number> ')
    
    if number != '':
        appendGlobal(number)
    else:
        flag = False

print(global_variable)
print(sortGlobal())