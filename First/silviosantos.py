#10 Write a Python program that iterates through integers from 1 to 100 and prints them. For integers that are multiples of three, print "Fizz" instead of the number. For integers that are multiples of five, print "Buzz". For integers which are multiples of both three and five print, "FizzBuzz".

for x in range(1, 100):
    print('')
    if (x % 3 == 0):
        print("Fizz", end='')
    
    if (x % 5 == 0):
        print("Buzz", end='')

    if (x % 3 != 0) and (x % 5 != 0):
        print(f'{x}', end='')