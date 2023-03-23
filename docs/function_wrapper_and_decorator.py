import time

#in python, functions are treated as objects

#1

def shout(text):
    return text.upper()

print(shout('Hello'))
print(type(shout))
yell = shout
print(yell('Hello'))


#function objects can be passed as arguments to other functions

#2

def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    greeting = func("""Hi, I am created by a function passed as an argument.""")
    print (greeting)

greet(shout)
greet(whisper)



# Functions can return another function
# we create a function inside of another function and then return the function created inside

#3

def create_adder(x):
    def adder(y):
        return x+y
    return adder

add_15 = create_adder(15)
print(add_15(10))


#Wrappers around the functions are also knows as decorators which are a very powerful and
#useful tool in Python since it allows programmers to modify the behavior of function or
#class. Decorators allow us to wrap another function in order to extend the behavior of the
#wrapped function, without permanently modifying it. In Decorators, functions are taken as
#the argument into another function and then called inside the wrapper function.

#4:

def hello_decorator(func):

    def inner1():
        print("Hello, this is before function execution")
        func()

        print("This is after function execution")
    return inner1


def function_to_be_used():
    print("This is inside the function !!")

func_obj = hello_decorator(function_to_be_used)


func_obj()


#5

#if we know the input of a function, we can give specific arguments to the :
#inner function

def twice(func):
    def inner(n):
        return func(func(n))
    return inner

def squarer(n):
    return n**2


twicer = twice(squarer)
print(twicer(3))






#5:
def timush(func):
    def inner(*args, **kwargs):
        print("I am going to run",func.__name__,"function")
        start = time.time()
        print(func(*args, **kwargs))
        end = time.time()
        print("the function",func.__name__, "took ", end-start, "seconds to calculate!")
        print("Bye bye")
    return inner
    
def summer(a,b):
    return a+b

funcer = timush(summer)
funcer(4,7)

#6:
#using the wrapper from #5 as a decorator
#decorators are used to modify the behaviour of function or class.
#In Decorators, functions are taken as the argument into another function and
#then called inside the wrapper function

@timush
def countdown(n):
    while n>0:
        n -= 1
     
print("now checking countdown")
countdown(10000000)



#7:
#another example of using a decorator chaining
def decor1(func):
    def inner():
        x = func()
        return x * x
    return inner

def decor(func):
    def inner():
        x = func()
        return 2 * x
    return inner

@decor1
@decor
def num():
    return 10

print(num())


#8:
#changing function input using decorators