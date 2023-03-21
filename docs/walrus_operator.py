#In this lesson, you’ll learn about the biggest change in Python 3.8:
#the introduction of assignment expressions. Assignment expression are
#written with a new notation (:=).This operator is often called the walrus
#operator as it resembles the eyes and tusks of a walrus on its side

#1
#Assignment expressions allow you to assign and return a value in the
#same expression. For example, if you want to assign to a variable and
#print its value, then you typically do something like this:

walrus = False
print(walrus)

print("-----------------")


#2
#In Python 3.8, you’re allowed to combine these two statements into one,
#using the walrus operator:

print(walrus := True)


print("-----------------")

#3
#One pattern that shows some of the strengths of the walrus operator is
#while loops where you need to initialize and update a variable. For
#example, the following code asks the user for input until they type quit:

inputs = list()
while True:
    current = input("Write something: ")
    if current == "quit":
        break
    inputs.append(current)
    
print(inputs)

print("-----------------")

#4
#now looks how it behaves with the Walrus operator


inputs = list()
while (current := input("Write something: ")) != "quit":
    inputs.append(current)
    
print(inputs)