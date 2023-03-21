#list comprehension and iterators
#used for code readibility

#list comprehension:
#1:
#regular way to make a certain list:
my_list = []
for x in range(10):
    my_list.append(2*x)
print(my_list)

#list comprehension way:
comp_list = [x*2 for x in range(10)]
print(comp_list)

#2 - a more intricate example of using list comprehension:
comp_list = [x**2 for x in range(7) if x%2==0]
print(comp_list)

#3 - combining 2 lists using list comprehension:
nums = [1, 2, 3, 4, 5]
letters = ['A', 'B', 'C', 'D', 'E']
one_to_one = [[nums[i], letters[i]] for i in range(len(letters))]
print(one_to_one)
#4 - making a whole combination from here and there:
nums_letters = [[n, l] for n in nums for l in letters]
print(nums_letters)

#5 - working with strings as well:
iter_string = "some text"
comp_list = [x for x in iter_string if x !=" "]
print(comp_list)

#6 - dictionary comprehension:
dict_comp = {x:chr(65+x) for x in range(1, 11)}
print(dict_comp)

#7 - set comprehension:
set_comp = {x ** 3 for x in range(10) if x % 2 == 0}
print(set_comp)



#iterable types
#Basically, any object that has iter() method can be used as an iterable. You can
#check using hasattr() function in the interpreter. To check just write the following:
#hasattr(type_of_object, '__iter__')

#Iterator protocol is implemented whenever you iterate over a sequence of data
#8 - using iterators:
simple_list = [1, 2, 3]
print(hasattr(type(simple_list), '__iter__'))
my_iterator = iter(simple_list)
print(my_iterator)
print(next(my_iterator))
print(next(my_iterator))
print(type(next(my_iterator)))


#9 - looping through an iterator using for

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x) 
  
  
#10 - Any and All methods are useful in checking if every element in the list#
#if they All or Any of the elements in the list satisfy the conditions.
 
lst = [4,6,8,12,16]
print(all(x%2==0 for x in lst))

#11 - example for any

print(any(x%2==1 for x in lst))


 
#12 - To create an object/class as an iterator you have to implement the
#methods __iter__() and __next__() to your object.
#The __iter__() method acts similar, you can do operations (initializing etc.),
#but must always return the iterator object itself.

#The __next__() method also allows you to do operations, and must return the
#next item in the sequence.

#To prevent the iteration to go on forever, we can use the
#StopIteration statement.

class MyNumbers:
  def __init__(self, limit):
      self.limit = limit
    
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.limit <= 0:
        x = self.a
        self.a += 1
        return x
        
    if self.a <= self.limit:
        x = self.a
        self.a += 1
        return x
    else:
        raise StopIteration

myclass = MyNumbers(0)
myiter = iter(myclass)

for x in myiter:
  print(x)
  if x>15:
      break