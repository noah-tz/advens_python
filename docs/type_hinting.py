#Like we have in C, or C++ where we need to identify the type of the variable,
#in Python there is a way to do it as well

#1

def add_hi(s : str):
    b = s + " hi"
    return b
    

print(add_hi("hello"))

#here we used a type hinting only for the input, but we can do it for the
#output as well   

#2

def add_hi2(s : str)->str:
    b = s + " hi"
    return b

print(add_hi2("hello"))

#3

def add_me(a:int ,b : int=0)->int:
    return a+b

print(add_me(6))
print(add_me(3,5))