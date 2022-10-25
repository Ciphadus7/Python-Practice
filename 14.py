string = input('Enter words with whitespaces(1 or more): ')

words = string.split()
print(words)

i = 0
for w in words:
    words[i] = w[::-1]
    i += 1

new_str = ' '.join(words)

print(new_str)
