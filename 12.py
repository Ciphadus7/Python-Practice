usr_input = str(input('Type a long sentence with spaces: '))

words_list = usr_input.split(' ')

words_reversed = ' '.join(reversed(words_list))

print(words_reversed)