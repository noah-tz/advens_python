#OOP access modifiers

#1
#consider the following class
#public access modifiers

class Car:
    year = None
    model = None

    def __init__(self, year, model):
        self.year = year
        self.model = model


car = Car(1997, "T")
car.year = 1998
car.model = "JAJAJAJA"



#2
#protected access modifiers

class Student:
# protected data members
    _name = None
    _roll = None
    _branch = None
    
#     # constructor
    def __init__(self, name, roll, branch):
        self._name = name
        self._roll = roll
        self._branch = branch


class Geek(Student):

# constructor
    def __init__(self, name, roll, branch):
        Student.__init__(self, name, roll, branch)

# public member function
    def displayDetails(self):
# accessing protected data members of super class
        print("Name: ", self._name)

# accessing protected member functions of super class
        self._displayRollAndBranch()

# creating objects of the derived class       
obj = Geek("R2J", 1706256, "Information Technology")
obj._name = "aviv"



#3
#private access modifiers

class Animal:
# private data members
    #__name = None
    #__action = None
    
    def __init__(self, name, action):
        self.__name = name
        self.__action = action
        
    def get_name(self):
        return self.__name
    
dog = Animal("rob", "bark")

#accessing name through a getter method
print(dog.get_name())

#cannot access the data member directly
dog.__name  #ERROR!!!