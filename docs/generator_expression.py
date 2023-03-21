from sys import getsizeof
#generator expressions

#In Python, generators provide a convenient way to implement the iterator protocol.
#Generator is an iterable created using a function with a yield statement.

#The main feature of generator expression is evaluating the elements on demand. When you
#call a normal function with a return statement the function is terminated whenever it
#encounters a return statement. In a function with a yield statement the state of the
#function is “saved” from the last call and can be picked up the next time you call a 
#generator function.

#first example:

def my_gen():
    for x in range(5):
        yield x

print(type(my_gen()))

#A Python generator expression is an expression that returns a generator
#(generator object).

#2
#using the generatםr:
lst = []
for a in my_gen():
    lst.append(a)
print(lst)

#3
# generator expression
# Generator expression in Python allows creating a generator on a fly without a yield
# keyword. However, it doesn’t share the whole power of generator created with a yield
# function. The syntax and concept is similar to list comprehensions:
gen_exp = (x ** 2 for x in range(10) if x % 2 == 0)
for x in gen_exp:
    print(x)

#4
#generator expression vs list comprehension
list_comp = [x ** 2 for x in range(100) if x % 2 == 0]
gen_exp = (x ** 2 for x in range(100) if x % 2 == 0)
print(list_comp)
print(gen_exp)
print(getsizeof(list_comp))
print(getsizeof(gen_exp))

#We can see this difference because while `list` creating Python reserves memory for
#the whole list and calculates it on the spot. In case of generator, we receive only
#”algorithm”/ “instructions” how to calculate that Python stores. And each time we
#call for generator, it will only “generate” the next element of the sequence on
#demand according to “instructions”.

#On the other hand, generator will be slower, as every time the element of sequence
#is calculated and yielded, function context/state has to be saved to be picked up
#next time for generating next value. That “saving and loading function 
#context/state” takes time.


