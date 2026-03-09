# [] create list-o-matic as a function and call it
# [] be sure to include your spelled-out name in the welcome prompt
# [] you are welcome to use any list you like for list-o-matic, does not have to be animals 

def list_o_matic(string,items):
    if string == '':
        poped_value = items.pop()
        return poped_value + ' poped from list'
    elif string.capitalize() in items:
        items.remove(string.capitalize())
        return '1 instance of ' + string.capitalize() + ' removed from list'
    else:
        items.append(string.capitalize())
        return '1 instance of ' + string.capitalize() + ' appended to list'
    
favorite_characters = ['Luno', 'Augusta', 'Cartethyia', 'Azusa', 'Kururu']
while favorite_characters:
    print('Welcome, Quang Huynh. Look at your favorite characters:',favorite_characters )
    user_input = input('Enter the name of your favorite character: ')
    if user_input.lower() == 'quit':
        print('Goodbye!')
        break
    else:
        print(list_o_matic(user_input,favorite_characters))

if favorite_characters == []:
    print('Goodbye!')




