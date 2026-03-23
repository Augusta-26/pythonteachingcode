def string_filter(quote):
    word = ''
    for character in quote:
        if character.isalpha():
            word += character
        else:
            if word != '': #handle case of string argument starting or/and ending with non-alpha characters 
                if word[0].lower() > 'g':
                    print(word.upper())
                word = ''
    if word != '': #handle case of string argument ending with alphabetical character
        if word[0].lower() > 'g':
            print(word.upper())
    
user_input = input('Welcome, Quang Huynh. Please enter one sentence quote, alpha seperate words: ')
string_filter(user_input)
   

    

    
    



