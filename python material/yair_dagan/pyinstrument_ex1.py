import random

"""Example 1: Simply Profiling Script
Our first example involves profiling results generation for a simple python script using Pyinstrument. 
We have created a simple python script which loops 1000000 times generating two random numbers, 
adding them to generate a sum, and then adding that sum to the list before returning the list. 
We have kept this script in a file named pyinstrument_ex1.py in a folder named profiling_examples. 
We'll be reusing the script in the future examples as well."""


def add(a, b):
    return a + b


def get_sum_of_list():
    final_list = []
    for i in range(1000000):
        rand1 = random.randint(1, 100)
        rand2 = random.randint(1, 100)
        out = add(rand1, rand2)
        final_list.append(out)
    return final_list


if __name__ == "__main__":
    l = get_sum_of_list()
#    print(l)
