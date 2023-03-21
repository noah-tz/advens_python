#Example of exceptions, raise,  try and catch


def do_not_exceed_10(x):
    if x>10:
        raise ValueError('x should not exceeed 10. The value was {}'.format(x))
    else:
        print("all good")

def must_be_exactly_10(a):
    assert(a==10), "The value must be 10. It was {}".format(a)

#main

#1
do_not_exceed_10(9)

#2
must_be_exactly_10(10)

#3
try:
    do_not_exceed_10(11)
except:
    print("Function call was invalid")
    
#4
try:
    must_be_exactly_10(11)
except AssertionError as error:
    print("Something went wrong... ")
    print(error)
    print("Function was not executed")
    
#5
try:
    do_not_exceed_10(10)
except:
    print("my number is bigger than 10")
else:
    print("running stuff after all went well")
finally:
    print("finished. print it in any case")

#6
x = "hello"

#if condition returns True, then nothing happens:
assert x == "hello"

#if condition returns False, AssertionError is raised:
assert x == "goodbye", "something is wrong. x = {} and is not goodbye".format(x)
