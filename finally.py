f = open('a.txt', 'r')


try:
    f.write('Write to this file.')
except Exception as e:
    print('There was an exception:', e)
finally:            #This code will be executed no matter
    print('This code is always executed')
    print('File closed: ', f.closed)
    f.close()

print('File closed: ', f.closed)
