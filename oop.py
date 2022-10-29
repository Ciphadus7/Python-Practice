class Robot:
    """
    This class implelements a Robot.
    """
    population = 0


    def __init__(self, name, year):
        self.name = name        #left hand side = attributes. right hand side = method parameter
        self.year = year        #by convention we use the same names for object attributes(next to self ) and method parameters(RHS)
        Robot.population += 1
    # def __del__(self):        #to delete the class
    #     print('Robot died.')

    def setEnergy(self, energy):    #common method to create a method
        self.energy = energy



r1 = Robot("Marvin", 2040)      #call

print(type(r1))

# print(r1.__doc__)
print('Robot name: ', r1.name)  #name of the obj (.) name of the attribute [no spaces of course] to access it
r1.setEnergy(100)           #set value and add it to the dictionary
print('Dictionary that stores the attributes: ', r1.__dict__)
print('Energy consumed: ', r1.energy)   #both of these are correct. choose w/e you want
# print('Energy consumed: ', getattr(r1, 'energy'))

print(getattr(r1, 'producer', 'Robot without producer'))    #It will try to get the attribute 'producer' from r1 instance and if it fails(which it will)
                                                            #it will print out 'Robot without producer'

r2 = Robot('Calvin', 2050)
r3 = Robot('David', 2030)

r1.population += 10

#Class attributes are attributes that are owned by the class itself. They will be shared by all instances. They have the same value

print('Robot Population : ', Robot.population)      #class attributes(like population here) is shared across all instances so it will output 3 as it looks at it globally
print('Robot Population : ', r1.population)         #will output 13 as we changed the instance's value 


