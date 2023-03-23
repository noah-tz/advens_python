#lambda functions

#lambdas are treated identically to regular functions at the interpreter level.
#In a way, you’ll say that lambdas provide compact syntax for writing functions
#that return one expression.

greet = lambda : print('Hello World')
greet()

x = lambda a : 2*a
print(x(5))

y = lambda a, b : a * b
print(y(4,7))

z = lambda a, b, c : a + b + c
print(z(5, 6, 2))

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)


print(mydoubler(11))
print(mytripler(11))


w = lambda a : print("hi, my number is "+ str(a))

w(68)



#can even use lambda functions with if statements. The syntax looks as follows:
#lambda <arguments> : <Return Value if condition is True> if <condition> else <Return Value if condition is False>

#the next function adds 1 if value => 0 and substracts 1 when value < 0 
k = lambda a: a+1 if a>=0 else a-1

print(k(-11.4))
print(k(15.6))

#The map function is employed to use a specific operation for each element in
#a sequence. It takes 2 parameters:

#1. A function that defines how the operations to be performed on the elements.
#2. One or more sequences.

def adder(n):
    return n+1

sequences = [10,2,8,7,5,4,11]
incremented_result = map (adder, sequences) 
print(list(incremented_result))

squared_result = map (lambda x: x*x, sequences) 
print(list(squared_result))


#finally we want to show what a filter does is filter out elements
#when using lambda

lst = [1,2,3,4,5,6,7]
iter_lst = filter (lambda x: (x%2==0), lst)
print(list(iter_lst))



