import math

# ex1
class Roman_namera:
    """it is class that convert int number to roman namera
    """

    def __init__(self, number: int) -> None:
        """AI is creating summary for __init__

        Args:
            number (int): [take int number and init the data of class]
        """
        self.__list_num_general = [1, 4, 5, 9, 10,
                                   40, 50, 90, 100, 400, 500, 900, 1000]
        self.__list_rom_num_general = ['I', 'IV', 'V', 'IX', 'X', 'XL',
                                       'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        self.__original_number = number
        self.__number = number
        self.__roman_num = ''
        self.__result = self.__convert_number()

    def __repr__(self) -> str:
        """AI is creating summary for __repr__

        Returns:
            str: [string of description of class]
        """
        return f"number is {self.__original_number} the converted to roman num is {self.__result}"

    def __convert_number(self):
        """AI is creating summary for __convert_number

        Returns:
            string: the converted of number of object
        """
        index_rom = 12
        while self.__number:
            count_div, self.__number = divmod(
                self.__number, self.__list_num_general[index_rom])
            for _ in range(count_div):
                self.__roman_num += self.__list_rom_num_general[index_rom]
            index_rom -= 1
        return self.__roman_num

    def get_rom(self):
        """AI is creating summary for get_rom

        Returns:
            string: the result converted of number of object
        """
        return self.__result


def main_task1():
    a = Roman_namera(3549)
    print(a.get_rom())
    print(a)


# ex2
class Roman_to_int:
    """ this class take string of rom namera then return int number converted 
    """

    def __init__(self, roman: str) -> None:
        """AI is creating summary for __init__

        Args:
            roman (str): init the data members of object
        """
        self.__value_rom = {'I': 1, 'V': 5, 'X': 10,
                            'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        self.__original_str = roman
        self.__num = 0
        self.__result = self.__convert_str()

    def __repr__(self) -> str:
        """AI is creating summary for __repr__

        Returns:
            str: description of data of object (rom string and number converted)
        """
        return f"string roman namera is {self.__original_str} the converted to number num is {self.__result}"

    def get_number(self) -> int:
        """AI is creating summary for get_number

        Returns:
            int: number converted of class
        """
        return self.__result

    def __convert_str(self) -> int:
        """AI is creating summary for __convert_str

        Returns:
            int: [number converted of class, by the value table]
        """
        index = 0
        if len(self.__original_str) == 1:
            return self.__value_rom[self.__original_str]
        while index < len(self.__original_str) - 1:
            if self.__value_rom[self.__original_str[index]] < self.__value_rom[self.__original_str[index + 1]]:
                self.__num += self.__value_rom[self.__original_str[index + 1]
                                               ] - self.__value_rom[self.__original_str[index]]
                index += 2
            else:
                self.__num += self.__value_rom[self.__original_str[index]]
                index += 1
        if self.__value_rom[self.__original_str[-2]] >= self.__value_rom[self.__original_str[-1]]:
            self.__num += self.__value_rom[self.__original_str[-1]]
        return self.__num


def main_task2():
    a = Roman_to_int("MMMDXLIX")
    print(a.get_number())
    print(a)

# ex3
class Check_closes:
    """
    this object take string that It is possible ther are parenthesis, and check if The arrangement of parenthesis is correct
    for example "(([(khkhvkhv)(jobjbub)]){(inogugiug)})" is corect, "(((liviyv)()]" is not correct
    """

    def __init__(self, get_str: str) -> None:
        """AI is creating summary for __init__

        Args:
            get_str (str): [string that class take for check]
        """
        self.__list_of_parenthesis = ['[', ']', '(', ')', '{', '}']
        self.__dict = {'[': ']', '(': ')', '{': '}'}
        self.__take_str = get_str
        self.__parenthesis = self.__init_str_of_parenthesis()
        self.__is_correct = self.__check_closes()

    def __init_str_of_parenthesis(self):
        """AI is creating summary for __init_str_of_parenthesis

        Returns:
            [type]: [A string containing only the parentheses, from the string that init received]
        """
        return "".join(char for char in self.__take_str if char in self.__list_of_parenthesis)

    def __check_closes(self) -> bool:
        """AI is creating summary for __check_closes

        Returns:
            bool: [The method checks whether the string is valid or not, and returns a boolean value]
        """
        stuck = []
        for parenthesis in self.__parenthesis:
            if parenthesis in self.__dict:
                stuck.append(parenthesis)
            elif len(stuck) and parenthesis != self.__dict[stuck.pop()]:
                return False
        return not stuck

    def check_correct(self):
        return self.__is_correct


def main_task3():
    a = Check_closes("(([(khkhvkhv)(jobjbub)]){(inogugiug)})")
    b = Check_closes("(((liviyv)()]")
    c = Check_closes("((()()")
    d = Check_closes("(()()]")
    print(a.check_correct())
    print(b.check_correct())
    print(c.check_correct())
    print(d.check_correct())

# ex4
class Find_possible_unique_subsets:
    """
    AI is creating summary for the object Find_possible_unique_subsets
    this object take arr of numbers end give all the possible permutations of sub arrays
    for example:
        input- [4, 5, 6]
        output- [[], [4], [5], [4, 5], [6], [4, 6], [5, 6], [4, 5, 6]]
    """
    def __init__(self, len_of_numbers: list[int]) -> None:
        """
        AI is creating summary for __init__
        init data members of object

        Args:
            len_of_numbers (list[int]): [len of numbers for find]
        """
        self.__len_of_numbers = len_of_numbers
        self.__list_of_results = self.__find_lists_of_results()

    def __find_lists_of_results(self) -> list[list[int]]:
        """AI is creating summary for __find_lists_of_results

        Returns:
            list[list[int]]: [find all possible unique subsets from a set, and append they to list, return the list]
            by recursion!
        """
        list_of_results = [[]]
        for new_number in self.__len_of_numbers:
            list_of_results += [Internal_list + [new_number]
                                for Internal_list in list_of_results]
        return list_of_results

    def get_result(self) -> list[list[int]]:
        """AI is creating summary for get_result

        Returns:
            list[list[int]]: [list of result of Permutations of the array]
        """
        return self.__list_of_results


def main_task4():
    a = Find_possible_unique_subsets([4, 5, 6])
    print(a.get_result())

# ex5
class Find_pair_element:
    """
    AI is creating summary for Find_pair_element
    take array with numbers, and target. find pair elements in the array that equal to target
    for example:
        input- [10,20,10,40,50,60,70], target=50
        output- [3, 4]
    """
    def __init__(self, list_of_numbers: list[int], target: int) -> None:
        """AI is creating summary for __init__

        Args:
            list_of_numbers (list[int]): [list of numbers for search]
            target (int): [the pair elements need to be equal to target]
        init the members of object
        """
        assert (
            list_of_numbers and type(list_of_numbers) == list
        ), f"{list_of_numbers} is not an array with members"
        self.__list_of_numbers = list_of_numbers
        self.__target = target
        self.__array_result = self.__find_elements()

    def __find_elements(self) -> list[int]:
        """AI is creating summary for __find_elements

        Returns:
            list[int]: [list with pair indexes in original array, that equal target]
        """
        new_sorted_array = sorted(self.__list_of_numbers)
        start_of_range = 0
        end_of_range = len(new_sorted_array) - 1
        # while all array has not been tested, and still no result has been found
        while (start_of_range != end_of_range and new_sorted_array[start_of_range] + new_sorted_array[end_of_range] != self.__target):
            if new_sorted_array[start_of_range] + new_sorted_array[end_of_range] < self.__target:
                start_of_range += 1
            else:
                end_of_range -= 1
        # return array with pair indexes of result
        return [self.__list_of_numbers.index(new_sorted_array[start_of_range]), self.__list_of_numbers.index(new_sorted_array[end_of_range])] if start_of_range != end_of_range else []

    def get_result(self) -> list:
        """AI is creating summary for get_result

        Returns:
            list: [result of search of object]
        """
        return self.__array_result

def main_task5():
    a = Find_pair_element([10,20,10,40,50,60,70], 50)
    print(a.get_result())


# ex6
class Find_three_element:
    """
    AI is creating summary for Find_three_element
    take array with numbers, and target. find three elements in the array that equal to target
    for example:
        input- [-25, -10, -7, -3, 2, 4, 8, 10]
        output- [[-10, 2, 8], [-7, -3, 10]]
    """
    def __init__(self, list_of_numbers: list[int]) -> None:
        """AI is creating summary for __init__

        Args:
            list_of_numbers (list[int]): [list of numbers for search]
        init the members of object
        """
        assert (
            list_of_numbers and type(list_of_numbers) == list
        ), f"{list_of_numbers} is not an array with members"
        self.__list_of_numbers = list_of_numbers
        self.__array_result = self.__find_elements()

    def __find_elements(self) -> list[list[int]]:
        """AI is creating summary for __find_elements

        Returns:
            list[list[int]]: [list with lists of all results of three indexes in original array, that equal target]
        """
        list_results = []
        new_sorted_array = sorted(self.__list_of_numbers)
        for index in range(len(new_sorted_array)):
            new_sub_array = new_sorted_array[:index] + new_sorted_array[index +1:]
            find_pair_element = Find_pair_element(new_sub_array, -new_sorted_array[index])
            pair_element = find_pair_element.get_result()
            if len(pair_element):
                pair_element = [new_sub_array[pair_element[0]], new_sub_array[pair_element[1]]]
                pair_element += [new_sorted_array[index]]
                pair_element.sort()
                list_results += [pair_element]
        return self.__Reducing_duplication_array(list_results) # Reducing duplication in the array

    def __Reducing_duplication_array(self, array: list) -> list:
        """
        AI is creating summary for __Reducing_duplication_array

        Args:
            array (list): [Reducing duplication in the array]

        Returns:
            list: [array with duplication]
        """
        list_result = []
        for item in array:
            if item not in list_result:
                list_result.append(item)
        return list_result

        
    def get_result(self) -> list:
        """AI is creating summary for get_result

        Returns:
            list: [result of search of object]
        """
        return self.__array_result

def main_task6():
    a = Find_three_element([-25, -10, -7, -3, 2, 4, 8, 10])
    print(a.get_result())


# ex7
class Power:
    """
    AI is creating summary for Power
    take number and power, calculate result
    """
    def __init__(self, number: float, power: float) -> None:
        """AI is creating summary for __init__

        Args:
            number (float): [number of basic]
            power (float): [power for calculate]
        init data members
        """
        self.__number = number
        self.__power = power

    def result(self) -> float:
        """AI is creating summary for result

        Returns:
            float: [result of object]
        """
        return pow(self.__number, self.__power)

def main_task7():
    a = Power(5, 3)
    print(a.result())


#ex8
class Revers_words:
    """
    AI is creating summary for Revers_words
    take string with word than revers to words
    for example:
        input- hello .py
        output- .py hello
    """
    def __init__(self, string: str) -> None:
        """AI is creating summary for __init__

        Args:
            string (str): [string to revers]
        """
        self.__string = string

    def revers_words(self) -> str:
        """AI is creating summary for revers_words

        Returns:
            str: [calculate of revers]
        """
        arr_result = self.__string.split()[::-1]
        return "".join(f"{word} " for word in arr_result)

def main_task8():
    a = Revers_words("hello .py")
    print(a.revers_words())


# ex9
class Uppercase_letters:
    """
    AI is creating summary for Uppercase_letters
    take string, turn all small caps
    """
    def __init__(self, string: str) -> None:
        self.__string = string
        self.__uper_string = string.upper()

    def __repr__(self) -> str:
        return f"the original string is '{self.__string}', the upper string is '{self.__uper_string}'"

    def get_result(self) -> str:
        return self.__uper_string
    
    
def main_task9():
    a = Uppercase_letters("hello world")
    print(a.get_result())
    print(a)


# ex10
class Rectangle:
    """AI is creating summary for Rectangle
    calculate area
    """
    def __init__(self, length: float, width: float) -> None:
        self.__length = length
        self.__width = width

    def area_calculation(self) -> float:
        """AI is creating summary for area_calculation

        Returns:
            float: [result of area calculation]
        """
        return self.__length * self.__width # return area

def main_task10():
    a = Rectangle(10, 20)
    print(a.area_calculation())

# ex11
class Circle:
    def __init__(self, radius) -> None: # היקף- קוטר * פאי, שטח- רדיוס * רדיוס * פאי
        self.__radius = radius

    def compute_area(self) -> float:
        """AI is creating summary for compute_area

        Returns:
            float: [result of area of circle]
        """
        return self.__radius ** 2 * math.pi

    def compute_perimeter(self) -> float:
        """AI is creating summary for compute_perimeter

        Returns:
            float: [result of perimeter of circle]
        """
        return self.__radius * 2 * math.pi

def main_task11():
    circle = Circle(10)
    print(circle.compute_area())
    print(circle.compute_perimeter())

# ex12
def get_class_name(instance: object) -> type:
    """AI is creating summary for get_class_name

    Args:
        instance (object): [object for check is name]

    Returns:
        type: [type of instance]
    """
    return instance.__class__.__name__

def main_task12():
    a = Circle(10)
    print(get_class_name(a))



def main():
    """
    main_task1()
    main_task2()
    main_task3()
    main_task4()
    main_task5()
    main_task6()
    main_task7()
    main_task8()
    main_task9()
    main_task10()
    main_task11()
    main_task12()
    """



if __name__ == "__main__":
    main()

#
