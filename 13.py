hypenated_input = str(input('Enter a hypen-seperated string: '))

words = hypenated_input.split("-")
sorted_words = sorted(words)
sorted_str = "-".join(sorted_words)

print(sorted_str)
