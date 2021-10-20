
def calc(**kwargs):
    if kwargs["op"] == '+':
        return kwargs["a"] + kwargs["b"]    
    if kwargs["op"] == '-':
        return kwargs["a"] - kwargs["b"]

def parser(formula):
    
    formulaList = []
    formulaList = formula.split(" ")

    for item in formulaList:
        if item == " ":
            formulaList.Remove(" ")
    len(formulaList)
    try:
        if len(formulaList) != 3:
            raise Exception("FormulaError", "3")
    except Exception as exc:
        print(f'There\'s an {exc.args[0]}: #{exc.args[1]}')
        exit()
    
    try:
        formulaList[0] = float(formulaList[0])
        formulaList[2] = float(formulaList[2])
    except Exception as exc:
        try:
            raise Exception("FormulaError", "2")
        except Exception as exc:
            print(f'There\'s an {exc.args[0]}: #{exc.args[1]}')
            exit()

    try:
        if (formulaList[1] != "+") and (formulaList[1] != "-"):
            raise Exception("FormulaError", "1")
    except Exception as exc:
        print(f'There\'s an {exc.args[0]}: #{exc.args[1]}')
        exit()

    return { "a" : formulaList[0], "op" : formulaList[1], "b" : formulaList[2] }

flag = True

while flag:
    flag == False
    formulaIn = input("Type a formula (e.g 1 + 1): ")

    if formulaIn == "": 
        print("Exiting...")
        exit()
    else:
        formulaOut = parser(formulaIn)
        result = calc(**formulaOut)
        print(f'Result: {result}')
        flag == True
