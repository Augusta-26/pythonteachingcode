import os

def get_names():
    count = 0
    guess_list = []
    while count < 5:
        user_input = input("enter the name of an element in Period Table's first 20 elements: ").strip()
        if user_input != '':
            if user_input.lower() in guess_list:
                print('"' + user_input + '" was already entered')
            else:
                guess_list.append(user_input.lower())
                count += 1
    return guess_list

# !curl method will not work in Python intepreter
# To fix this, we import os library
# Put the shell command in a variable called cmd, then calling os.system(cmd)

cmd = "curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt -o elements1_20.txt"
os.system(cmd) 

elements1_20_file = open('elements1_20.txt','r')

elements1_20_list = []
element_name = elements1_20_file.readline().strip(' \n')
while element_name:
    elements1_20_list.append(element_name.lower())
    element_name = elements1_20_file.readline().strip(' \n')

elements1_20_file.close()

print("Welcome Quang Huynh - list any 5 of the first 20 elements in the Period table:")
quiz_responses = get_names()

correct_responses = []
incorrect_responses = []

for response in quiz_responses:
    if response.lower() in elements1_20_list:
        correct_responses.append(response.title())
    else:
        incorrect_responses.append(response.title())

grade = len(correct_responses) * 20
correct_responses_string = ' '.join(correct_responses)
incorrect_responses_string = ' '.join(incorrect_responses)

print(grade, "% correct")
print("Found:", correct_responses_string)
print('Not Found:', incorrect_responses_string)
