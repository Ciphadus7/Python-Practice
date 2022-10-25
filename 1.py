price = 50
balance = 90

if balance >= price:
    print(f'You can buy this product and your new balance will be {balance - price}')
else:
    print(f'Insufficent funds. Please deposit {price - balance}')


answer = input('Do you want to continue? Enter yes or no')
if answer.lower() == 'yes':
    print('We\'ll move on')
elif answer.lower() == 'no':
    print('We\'ll stop')
else:
    print('Invalid Answer')
