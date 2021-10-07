#02 Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them. 

def reverse_name(name):
    reversed_name = []
    for word in name:
        reversed_name.append(word[::-1])
    
    return reversed_name
    

text_input = ''

while text_input != '':
    print(f'Write your full name or enter to exit:')
    
    text_input = input(f'> ')
    
    if text_input == '0':
        exit()

    fullName = text_input.split()

    eman_desrever = reverse_name(fullname)

    for eman in eman_desrever:
        print(eman + ' ', end='')
