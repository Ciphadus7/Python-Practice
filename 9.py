number = int(input('Please type a number: '))
divisors = list()

for i in range(2, number //2+1):
    if number % i == 0:
        divisors.append(i)
    
print(divisors)
