from termios import B75


a = 9
b = int(input('Enter b: '))

# b = str(b)     This is for type error as we're converteing the inputted integer to a string and arithemtic operations between integers and strings raise an exception
# del b         This is for 'Exception' as those exceptions can be anything except typeerror and zerodivisionerror

try:
    c = a / b
except ZeroDivisionError as e:                                 
    print('Division by zero is not allowed! Exception raised: ', e)
except TypeError as e:
    print('a and b must be numbers. Exception rasied: ', e)
except Exception as e:
    print('Another unspecified error. Exception raised: ', e)
else:               
    print('No error.')
    print(f'c = {c}')

print('Other code starts here. Continue Execution....')
for x in range(10):
    print(x, end=' ')