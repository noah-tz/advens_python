from datetime import date
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
avi.incrementBy(4)
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
Person2.increment = classmethod(Person2.incrementBy)
    
avi = Person2()
avi.printAge()
#can call by class definition
Person2.increment(4)
avi.printAge()

print("------------------------------------------------------------------")

#3
#consider the following class
#we can use the classmethod as a decorator and get the same result with less
#syntax

class Person3:
    age = 25
    #this decoratorr is defined inside the class
    @classmethod
    def printAge(cls):
        print('The age is:', cls.age)
    @classmethod
    def incrementBy(cls, n):
        cls.age += n


avi = Person3()
avi.printAge()
#can call by class definition
Person3.incrementBy(4)
avi.printAge()

print("------------------------------------------------------------------")

#4
#consider the following class
#we can use classmethod for instatiation of new elements

class Person4:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)


    def display(self):
        print(self.name + "'s age is: " + str(self.age))

person = Person4('Adam', 19)
person.display()

person1 = Person4.fromBirthYear('John',  1985)
person1.display()