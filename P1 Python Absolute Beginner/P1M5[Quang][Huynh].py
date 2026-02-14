def adding_report(report='T'):
    items = ''
    total = 0
    print('enter a digit to add to the total or "Q" to quit')
    while True:
        user_input = input('enter an integer or "Q": ')
        if user_input.isdigit():
            total += int(user_input)
            if report.upper() == 'A':
                items += user_input + '\n '
        elif user_input.upper() == "Q" or user_input.upper() == 'QUIT' or user_input.upper().startswith('Q'):
            if report.upper() == "A":
                print('Items\n',items)
            print('Total\n',total,'\n Calculated by: Quang Huynh')
            break
        else:
            print(user_input,'is invalid input')

adding_report('A')
adding_report()





    

        


