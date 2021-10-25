def decor(func):
    
    def capsule(val):
        funct = val + 1
        return funct

    return capsule

@decor
def sum(a):
    return a + 2 * a

result = sum(2)

print(result)