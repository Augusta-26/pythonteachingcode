quote = input('Welcome, Quang Huynh. Please enter one sentence quote, alpha seperate words: ')
word = ''

for character in quote:
    if character.isalpha():
        word += character
    else:
        if word != '':
            if word[0].lower() >= 'h':
                print(word.upper(),)
                word = ''
            else:
                word = ''
if word != '':
    if word[0].lower() >= 'h':
        print(word.upper())