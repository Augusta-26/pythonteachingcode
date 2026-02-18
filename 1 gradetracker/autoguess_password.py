
'''
Right now it guesses the entire word randomly every time.
'''
pass_word = 'aug'
import random

character = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
guess = ''
try_total = 0

while guess != pass_word:
    guess = ''
    for i in range(len(pass_word)):
        random_letter = random.choice(character)
        guess += random_letter
    try_total += 1
    print(f"try #{try_total}: {guess}")

print(f"correct password #{try_total} is '{guess}'")



'''
version of more efficient, keep correct letters
'''
import random

pass_word = 'chico'
characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

guess = [''] * len(pass_word)
try_total = 0

while ''.join(guess) != pass_word: # join function combines elements of a list into a string
    for i in range(len(pass_word)):
        if guess[i] != pass_word[i]:
            guess[i] = random.choice(characters)
    
    try_total += 1
    print(f"try #{try_total}: {''.join(guess)}")

print(f"\nPassword cracked in {try_total} tries!")

'''
Version With Uppercase + Numbers
'''
'''
Version With Uppercase + Numbers
'''
import random
import string #string module contains collection of string constants

pass_word = 'chico'
character = string.ascii_letters + string.digits
guess = [''] * len(pass_word)
try_total = 0

while ''.join(guess) != pass_word:
    for i in range(len(pass_word)):
        if guess[i] != pass_word[i]:
            guess[i] = random.choice(character)
    try_total += 1
    print(f"try # {try_total}: {''.join(guess)}")

print(f"guess successfully at try#{try_total}: {''.join(guess)}")




