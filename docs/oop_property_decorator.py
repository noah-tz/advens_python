#OOP property decorator

#1
#consider the following classs
class Student:
    def __init__(self, first_name):
        self.__first_name = first_name

    # define getter method
    def get_name(self):
        return self.__first_name
    
    # define setter method
    def set_name(self, name):
        if type(name) == str:
            self.__first_name = name
        else:
            print("please input a valid name")
            
            
# create a new Student object
student = Student("Monica")

# access the first name using getter and setter
print(student.get_name())  # Monica
student.set_name("Avi")
print(student.get_name())

print("----------------------------------------------")

#2
#we now use the property decorator to the same class, to do the getter function
#but much more comfortably

#consider the following classs
class Student2:
    def __init__(self, first_name):
        self.__first_name = first_name

    # define getter method with property decorator
    @property
    def name(self):
        return self.__first_name
    
    # define setter method
    def set_name(self, name):
        if type(name) == str:
            self.__first_name = name
        else:
            print("please input a valid name")


# create a new Student object
student2 = Student2("Monica")

# access the first name using property decorator
print(student2.name)  # Monica
student2.set_name("Avi")
print(student2.name)


print("----------------------------------------------")

#3
#we now use the property decorator to the same class, to do the setter function

#consider the following classs
class Student3:
    def __init__(self, first_name):
        self.__first_name = first_name

    # define getter method with property decorator
    @property
    def name(self):
        return self.__first_name
    
    # define peoperty setter method 
    @name.setter
    def name(self, name):
        if type(name) == str:
            self.__first_name = name
        else:
            print("please input a valid name")

#Now we can look at name as if it is a "public" variable. But in fact it is not.
#We have a check if the input is valid although it doesn't seems like it.

# create a new Student object
student3 = Student3("Monica")

# access the first name using property decorator
print(student3.name)  # Monica
student3.name = 33242 #setter property
student3.name = "Avi" #setter property

print(student3.name)

print("----------------------------------------------")

#4
#delete method to delete a data type


#consider the following classs
class Student4:
    def __init__(self, first_name):
        self.__first_name = first_name

    # define getter method with property decorator
    @property
    def name(self):
        return self.__first_name
    
    # define peoperty setter method 
    @name.setter
    def name(self, name):
        if type(name) == str:
            self.__first_name = name
        else:
            print("please input a valid name")
    # define a "name" deleter

    @name.deleter
    def name(self):
        del self.__first_name
        
# create a new Student object
student4 = Student4("Monica")

# access the first name using property decorator
print(student4.name)  # Monica
student4.name = 33242 #setter property
student4.name = "Avi" #setter property
#delete property
del student4.name
try:
    print(student4.name)
except:
    print("could not enter name")
    
    
print("----------------------------------------------")

#5
#the property method is in fact can be used without a decorator, but just as
#a function. Here is the syntax:
#Syntax: property(fget, fset, fdel, doc)

#fget() – used to get the value of attribute
#fset() – used to set the value of attribute
#fdel() – used to delete the attribute value
#doc() – string that contains the documentation (docstring) for the attribute

class Alphabet:
    def __init__(self, value):
        self._value = value
        
    # getting the values
    def getValue(self):
        print('Getting value')
        return self._value
    
    # setting the values
    def setValue(self, value):
        print('Setting value to ' + value)
        self._value = value
        
    # deleting the values
    def delValue(self):
        print('Deleting value')
        del self._value
        
    value = property(getValue, setValue, delValue, )

# passing the value
x = Alphabet('GeeksforGeeks')
print(x.value)

x.value = 'GfG'

del x.value