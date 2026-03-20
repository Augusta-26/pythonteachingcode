def word_mixer(orginal_list):
    orginal_list.sort()
    new_list = []
    while len(orginal_list) > 5:
        popped_value_1 = orginal_list.pop(-5)
        new_list.append(popped_value_1)
        popped_value_2 = orginal_list.pop(0)
        new_list.append(popped_value_2)
        popped_value_3 = orginal_list.pop(-1)
        new_list.append(popped_value_3)
    return new_list

string_input = input('Welcome Quang Huynh. Please enter a poem: ')
poem_words = string_input.split()
for i in range(len(poem_words)):
    if len(poem_words[i]) <= 3:
        poem_words[i] = poem_words[i].lower()
    elif len(poem_words[i]) >= 7:
        poem_words[i] = poem_words[i].upper()

mixed_words = word_mixer(poem_words) #returned list from function
modified_poem = ' '.join(mixed_words) #convert returned list to string with space
print(modified_poem)