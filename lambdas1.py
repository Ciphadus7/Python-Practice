def square(x):
    return x ** 2
print(square(5))

sq2 = lambda x=1: x ** 2        #can assign a default value to the parameter but NOT to the expression
print(sq2())

sq = lambda x: x ** 2            #square() has the same logic as this lambda statement
print(sq(5))

s = lambda x,y : x + y
print(s(5,7))



def my_function(x, func):          #Example of a function that takes another function as an arguement
    return func(x)

y = my_function(5, lambda x: x ** 2)
print(y)