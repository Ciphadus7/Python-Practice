class Robot:

    population = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Robot.population += 1
    
    def __str__(self):
        my_str = 'My name is ' + self.name + ' and my price is ' + str(self.price)
        return my_str

    def __add__(self, other):
        price = self.price + other.price    
        return price

r1 = Robot('Marvin', 150)
r2 = Robot('Calvin', 100)

print(r1)

print(r1 + r2)  #This will now work because you've added the __add__ method