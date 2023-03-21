import math


# Class exercises


# return permuted matrix
def replace_matrix(matrix: list[list[any]]) -> list[list[any]]:
    return [[row[column] for row in matrix] for column in range(len(matrix[0]))]


# Returns an array of prime numbers from 2 to n
def find_primes_ton(n: int) -> list[int]:
    return ([2] + [prime for prime in range(3, n + 1, 2) if all(prime % number != 0 for number in range(3, int(prime ** 0.5)))]) if n >= 2 else []


# Returns the sub-array from the number after the first odd number to the end
def print_from_Odd(arr: list[any]) -> list[any]:
    return arr[[index for index in range(len(arr)) if arr[index] % 2 != 0][0] + 1:] if any(number % 2 != 0 for number in arr) else []


def sqr_gen(number: int):  # return all the numbers from 1 to n where there are two numbers whose squares are equal to n
    return list((num for num in range(number + 1) if any(num
                                                         for number1 in range(1, math.ceil(math.sqrt(num)) + 1)
                                                         for number2 in range(1, math.ceil(math.sqrt(num)) + 1)
                                                         if num == number1 ** 2 + number2 ** 2)))


# return Checks for error in the array and converts them to -1
def check_arr_of_numbers(range_check: int) -> list:
    def check_number(some_number: int):
        if some_number % 2 == 0:
            return some_number ** 2
        raise ValueError
    my_list = []
    for number in range(range_check + 1):
        try:
            my_list.append(check_number(number))
        except Exception:
            my_list.append(-1)
    return my_list


# return Checks for errors in tow types in the array and converts them to -1 and -2
def check_arr_of_ages(arr: list[any]) -> list[int]:
    def check_age(age: float):
        if age >= 15 and age <= 80:
            if type(age) == int:
                return age
            raise RuntimeError
        raise ResourceWarning
    my_list = []
    for age in arr:
        try:
            my_list.append(check_age(age))
        except RuntimeError:
            my_list.append(-1)
        except ResourceWarning:
            my_list.append(-2)
    return my_list


def main():
# Class exercises
    """
    # ex1
    # print(replace_matrix([[5,3,1] ,[2,3,6] ,[7,5,7] ,[2,9,6]]))
    # ex2
    print(find_primes_ton(10))
    # ex3
    print(print_from_Odd([2, 4, 6, 5, 22, 77, 89]))
    print(sqr_gen(100))
    print(check_arr_of_numbers(50))
    print(check_arr_of_ages([12, 15, 11.2, 15.3, 40.5, 70, 80, 80.3, 85, 88.2]))
    """
    
    

if __name__ == '__main__':
    main()
