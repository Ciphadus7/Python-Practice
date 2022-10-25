x = 0

while x < 10:
    print(f'The current value of x is {x}')
    x = x + 1       #x += 1
else:
    print(f'This is the else statement. x is not less than 10. x is {x}')
    


y = 12

while y < 100:
    y += 1
    if y % 13 != 0:  
        continue
    print(y)


while True:
    guess = input('Guess a lucky number before 1 and 10: ')
    if int(guess) == 8:
        print('You won!')
        break
    print(f'{guess} was not a lucky number!')




for letter in 'word':
    i = 3
    while i > 0:
        i -= 1
        print(letter, end='')
    print('')