#generator functions

#Python provides a generator to create your own iterator function. A generator
#is a special type of function which does not return a single value, instead,
#it returns an iterator object with a sequence of values. In a generator
#function, a yield statement is used rather than a return statement. The
#following is a simple generator function.


#1


def mygenerator():
    print('First item')
    yield 10

    print('Second item')
    yield 20

    print('Last item')
    yield 30

gen = mygenerator()
print(type(gen))
a = next(gen)
print(a)
next(gen)
next(gen)


#The generator function cannot include the return keyword. If you include it,
#then it will terminate the function. The difference between yield and return
#is that yield returns a value and pauses the execution while maintaining the
#internal states, whereas the return statement returns a value and terminates
#the execution of the function.
print("---------------")

#2



def mygenerator():
    print('First item')
    yield 10

    return

    print('Second item')
    yield 20

    print('Last item')
    yield 30

gen = mygenerator()
next(gen)
try:
    next(gen)
except:
    print("an exception occured")
    
    
    
print("---------------")

#3
def get_sequence_even_upto(x):
    for i in range(1, x+1):
        if i%2==0:
            yield i
            
seq = get_sequence_even_upto(10)

while True:
    try:
        print ("Received on next(): ", next(seq))
    except StopIteration:
        print("finished iterations")
        break
    
    
print("--------------")


#The generator is called just like a normal function. However, its execution is
#paused on encountering the yield keyword. This sends the first value of the
#iterator stream to the calling environment. However, local variables and their
#states are saved internally. 


#4 - second version of 3

#We can use the for loop to traverse the elements over the generator.
#In this case, the next() function is called implicitly and the StopIteration
#is also automatically taken care of.


        
        
seq = get_sequence_even_upto(6)


for elt in seq:
    print(elt)
    
print("--------------")



#5

#generator class is also very common, just need to do __iter__ and __next__
#function overloading

#look at this
#https://stackoverflow.com/questions/42983569/how-to-write-a-generator-class
class MySimpleRangeMinimal:
    def __init__(self, start: int, stop: int):
        self.start = start
        self.stop = stop
        self.i = self.start

    def send(self, value):
        if self.i < self.stop:
            out = self.i
            self.i = self.i + 1
            return out
        raise StopIteration

    def __next__(self):
        return self.send(None)

    def __iter__(self):
        return self