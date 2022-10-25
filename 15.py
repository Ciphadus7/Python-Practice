string = input('Enter words with whitespaces(1 or more): ')

words = string.split()

words = [w[::-1] for w in words]

new_str = ' '.join(words)

print(new_str)
    