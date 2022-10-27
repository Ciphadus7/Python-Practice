def is_prime(n):
    prime = True
    if n == 1:
        return False #1 is not a prime number
    i = 1
    while i < n // 2:
        i = i + 1
        if n % i != 0:
            prime = True
            break
    return prime #returns true or false

while True:
    print(is_prime(int(input('Please enter a number to check whether it\'s a prime number or not: '))))

