t1 = tuple(range(100))  #Built in names = tuple, range, print
print(t1)               #Global names = t1

x = 10                  #global variable
print(x)

def my_func():
    x = 5                                   #Local variable <---
    print(f'x inside the function {x}')     #Since its in a function, python tries to find the variable 'x'
                                            #inside a function but since its not there, it finds the global
my_func()                                   #variable instead

a = 10

def my_func1(b):
    global a                                #Thats how you use a global variable inside a function
    a += b
    print(f'a inside the function {a}')

my_func1(7)

print(f'a outside the function {a}')


def my_func2():
    print(x)    #looks for x in the global scope
    # x = 8     # ---> Returns an error since we are printing before creating a variable

my_func2()


print(len('abc'))

def len(x):     #Python considered len in the global namespace and not in the built-in namespace and thats  
    print(x)    #why it doesn't work according to its built-in functionality. NEVER USE NAMES THAT ARE ALREADY DEFINED

len('123456')

del len         #Deletes the len function defined above

print(len('asdhadbasjdjasbd'))