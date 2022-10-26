
######################################POSITIONAL ARGS######################################
def my_function1(a, b):         #THESE ARE POSITIONAL ARGUEMENTS. COS THEY LOOK AT THE POSITION OF THE 
    print(f'a is {a}')          #ARGUEMENT AND ASSIGNS IT TO THE SAME PARAMETER AT THE SAME POSITION.
    print(f'b is {b}')

my_function1(10, 5)



######################################DEFAULT ARGS######################################

def my_function2(a, b=10, c=9):      #IF WE ASSIGN A DEFAULT VALUE TO 'b' THEN WE HAVE TO ASSIGN A DEFAULT VALUE   
    print(f'a is {a}')             #TO 'c' AS WELL
    print(f'b is {b}')
    print(f'c is {c}')

my_function2(5, 30)


######################################KEYWORD ARGS######################################

def my_function3(a, b, c):      #A FUNCTION WITH KEYWORD ARGUEMENTS IS DEFINED THE SAME WAY AS A FUNCTION WITH  
    print(f'a is {a}')          # POSITIONAL ARGUEMENTS. THEIR ORDER DOESN'T MATTER. THE DIFFERENCE IS IN CALLING THE FUNCTION
    print(f'b is {b}')          #IF WE USE A KEYWORD ARGUEMENT FOR THE FIRST PARAMETER THEN WE NEED TO USE IT FOR THE OTHERS TOO
    print(f'c is {c}')          #IF NOT, THEN PYTHON WILL THROW AN ERROR. A POSITIONAL ARG IS NOT ALLOWED TO FOLLOW A KEYWORD ARG

my_function3(b=5, a=6, c=7 )

 
######################################*args ARGS######################################
                                #The name args is a convention. As long as the single asterisk is there, the meaning stands.
def f1(a, *args):               #WE DO THIS WHEN WE DON'T KNOW HOW MANY PARAMETERS YOU'RE GONNA NEED
    print(f'a: {a}')            #THEY USE POSITIONAL ARGUEMENTS.
    print(f'args: {args}')
    s = a + sum(args)           #ARGS IS A TUPLE
    print(f'Sum: {s}')

f1(5, 4)                        #SO WHILE CALLING THE FUNCTION, THE ARGUEMENTS WILL BE PASSED BASED ON POSITIONS


######################################**kwargs ARGS######################################

def f2(**kwargs):               #The name kwargs is a convention. As long as the double asterisk is there, the meaning stands.
    print(kwargs)               #CREATE A DICTIONARY OUT OF THE ARGUEMENTS(KEY: VALUE PAIRS)
    if 'name' in kwargs:        #Checking to see if the key 'name' is in the arguements passed
        print(f'Your name is {kwargs["name"]}') #Prints the value associated with the key

f2(name='John', age=40, location='London')    #This is how you pass an arguement with **kwargs

