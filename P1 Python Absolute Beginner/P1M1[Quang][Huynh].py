# Create name check code

# [ ] get input for input_test variable
input_test = input('Enter the names of people met in the last24 hours: ').lower()
# [ ] print "True" message if "John" is in the input or False message if not
print("'John' is in the input:", 'John'.lower() in input_test)


# [ ] print True message if your name is in the input or False if not
print("'Quang' is in the input:", 'Quang'.lower() in input_test)


# [ ] Challenge: Check if another person's name is in the input - print message
print('"Bob" is in the input:', "Bob".lower() in input_test)


# [ ] Challenge: Check if a fourth person's name is in the input - print message
print('"Anna" is in the input:', "Anna".lower() in input_test)