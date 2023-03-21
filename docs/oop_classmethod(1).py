#OOP classmethod

#1
#consider the following class
#age is the class variable, it does not depend on objects of the class, but it
#is rather joint to all. It uses the 'cls' word to tell it that it wants to 
#call the class variable
class Person:
    age = 25

    def printAge(cls):
        print('The age is:', cls.age)

    def incrementBy(cls, n):
        cls.age += n
        

avi = Person()
avi.printAge()

print("------------------------------------------------------------------")

#2
#consider the following class
#it is almost the same, but now we use the reserved classmethod() function.
#This enables us to call the class method without using a specific instance of
#the class, but rather directly by using the class name.

class Person2:
    age = 25

    def printAge(cls):
        print('The age is:', cls.age)

    def incrementBy(cls, n):
        cls.age += n
        
#notice this is defined outside the class
Person2.printAge = classmethod(Person2.printAge)
    
avi = Person2()
avi.printAge()

#TBD - add decorator examples