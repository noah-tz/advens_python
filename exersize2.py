import math
import random
#ex1
def abs_number(number: float) -> float: # return sqrt of absolute number
    lambda_function = lambda number: abs(number) ** 0.5
    return lambda_function(number)

#ex2
def make_double(arr: list[int]) -> list[int]: # make event all the odd element without function
    return [math.ceil(double/2) * 2 for double in arr]


def make_double2(arr: list[int]) -> list[int]: # make event all the odd element with function
    def addition(n):
        return n if n % 2 == 0 else n + 1
    return list(map(addition, arr))


def make_double3(arr: list[int]) -> list[int]: # make event all the odd element with lambda
    map_ = lambda number: number if number % 2 == 0 else number +1
    return [map_(i) for i in arr]

#ex3
def Decorator(func):
    def change_func(*args, **kwargs):
        return func(*args, **kwargs) ** 2
    return change_func


@Decorator
def root_abs_number(number: float) -> float:  # return root of absolute number
    return math.sqrt(abs(number))

#ex4
def decorator_mult(func):
    def mult_arr(*args):
        result = 1
        for i in args[0]:
            result = func(i, result)
        return result
    return mult_arr
@decorator_mult
def mult(number1: int, number2  = 1) -> int:
    return number1 * number2

#ex5
def points_on_circular(radius: float, center: float = 0) -> list[list[float]]: # take radius of circular and center of circular and return tow random points on circular
    angle1 = random.randrange(1, 360)
    angle2 = random.randrange(1, 360)
    return [center + radius * math.cos(angle1), center + radius * math.sin(angle1)], [center + radius * math.cos(angle2), center + radius * math.sin(angle2)]

#ex6
def gap_between_two_functions(func1, func2): 
    def wrapper(list_of_numbers: list[float]) -> list: # return the gap between tow functions
        return [abs(func1(number) - func2(number)) for number in list_of_numbers]
    return wrapper

def divide_number(number: float) -> float:
    return number / 2

#ex7
class Int_or_Float: # constructor
    def __init__(self, start_range: int, end_range: int) -> None:
        self.start_range = start_range
        self.end_range = end_range
        self.ret_int = True

    def return_random(self) -> any: # if random mode return random int, else return random float
        while True:
            yield random.uniform(self.start_range, self.end_range) if self.ret_int else random.randint(self.start_range, self.end_range)
        
def check_class() -> None: # test for class Int_or_Float
    a = Int_or_Float(10, 20)
    b = a.return_random()
    print(next(b))
    a.ret_int = False
    print(next(b))
    
#ex8
def sort_arrays(arr: list[list[any]]) -> list[list[any]]: # return sorted arr by key- the first member
    arr.sort(key = lambda Internal_array: Internal_array[0])
    return arr
def sort_array2(arr: list[list[any]]) -> list[list[any]]: # return sorted arr by key- the length internal_array
    arr.sort(key = lambda Internal_array: len(Internal_array))
    return arr

#ex9
def ret_lambda(number1: int, number2: int, number3: int): # return lambda for calculate polinom from a, b and c
    return lambda x: number1 * (x ** 2) + number2 * x + number3

#ex10
def map_function(list1: list, list2: list) -> list: # return all numbers in list1 in power of same index in list2, through map
    fun_calculate = lambda x, y: x ** y
    return list(map(fun_calculate, list1, list2))

#ex11
def filter_function(list1: list) -> list:
    fun_calculate = lambda x: x > 0
    return [root_number ** 0.5 for root_number in filter(fun_calculate, list1)]



def main():
    """
    # ex1
    print(abs_number(-10))
    # ex2
    print(make_double([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(make_double2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(make_double3([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    # ex3
    print(root_abs_number(-10))
    # ex4
    print(mult([3,6,2,5]))
    # ex5
    print(points_on_circular(5))
    # ex6
    print(gap_between_two_functions(abs_number, divide_number)([-5, 12, 20, -20, 15]))
    # ex7
    check_class()
    # ex8
    print(sort_arrays([[5, 3], [9, 2, 1], [3, 7, 1, 2], [3,7,1,2], [5, 3], [9,2,1]]))
    print(sort_array2([[5, 3], [9, 2, 1], [3, 7, 1, 2], [3,7,1,2], [5, 3], [9,2,1]]))
    # ex9
    print(ret_lambda(10, 20, 30)(5))
    # ex10
    print(map_function([3, 2, 1], [4, 5, 6]))
    # ex11
    print(filter_function([2, -5, 3, 4, -6, 10]))"""








if __name__ == '__main__':
    main()
