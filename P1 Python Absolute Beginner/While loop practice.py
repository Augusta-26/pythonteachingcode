def str_analysis(characters):
    if characters.isalpha():
        print('"' + characters + '" is all alphabetical characters')
    elif characters.isdigit():
        num = int(characters)
        if num > 100:
            print(characters,'is a big number')
        else:
            print(characters,'is smaller than expected')
    else:
        print('"' + characters + '" is mixed characters')

while True:
    user_input = input('enter anything except empty string: ')
    if user_input != '':
        str_analysis(user_input)
        break