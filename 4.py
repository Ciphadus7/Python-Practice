for number in range(10):
    if number == 5:
        break
    print(number)

print('Instruction outside for loop')

for letter in 'Python':
    print(letter)
    if letter =='o':
        break

for x in range(1, 20):
    if x % 13 == 0:
        break
else:
    print('There is no number divisible by 13 in the range.')


    
movies = ['LOTR', 'Madagascar', 'Toy Story', 'Frozen']

for m in movies:
    print(f'This is one of my favourite movies: {m}')
else:
    print('This is the end of the list.')