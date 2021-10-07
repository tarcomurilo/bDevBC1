#01 Write a Python program to test whether a passed letter is a vowel or not. 

def test_vowel(vowels, letter):
    for vowel in vowels:
        if vowel == letter:
            return True
    
    return False

letter = ''

while letter != '0':
    print(f'Write a letter or type 0 to exit:')

    letter = input(f'> ')
    print(letter)
    vowels = 'AaEeIiOoUu'

    if test_vowel(vowels, letter):
        print(f'It\'s a vowel!')
    else:
        print(f'It\'s not a vowel...')
