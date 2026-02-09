def str_analysis(text):
    if text.isdigit():
        num = int(text)
        if num > 99:
            return text + ' is a pretty big number' 
        else:
            return text + ' is a smaller number than expected'                
    elif text.isalpha():
        return '"' + text + '" is all alphabetical letters!'
    else:
        return '"' + text + '" is neither all alphabetical nor all digit!'

while True:
    user_input = input("Quang Huynh, enter word or integer: ")
    if user_input != "":
        print(str_analysis(user_input))
        break