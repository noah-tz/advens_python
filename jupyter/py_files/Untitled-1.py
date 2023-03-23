# %%
"""
1
Write a Python program that accepts a comma-separated sequence of words as input and prints the distinct words in sorted form (alphanumerically).

INPUT: red, black, green

OUTPUT: black, green,red
"""

# %%
def sort_words(string: str) -> str:
    """AI is creating summary for sort_words

    Args:
        string (str): [a comma-separated sequence of words]

    Returns:
        str: [A sequence of sorted words separated by commas]
    """
    list_of_sorted_words = string.split()
    list_of_sorted_words[-1] += ',' if list_of_sorted_words[-1][-1] != ',' else ''
    list_of_sorted_words.sort()
    list_of_sorted_words[-1] = list_of_sorted_words[-1][:-1]
    return ' '.join(list_of_sorted_words) # replace to string

print(sort_words("red, black, green,"))

# %%
""""
2
Write a Python program to print the following numbers up to 2 decimal places.
INPUT: 
x = 3.1415926
y = 12.9999

OUTPUT: 
Formatted Number:       3.14
Formatted Number:      13.00
"""

# %%
def split_vector(x: float, y: float) -> float:
    """AI is creating summary for split_vector

    Args:
        x (float): [x of vector, for example 3.1415926]
        y (float): [y of vector, for example 12.9999]

    Returns:
        float, float: [splitted numbers, for example (3.14, 13.0)]
    """
    x = round(x, 2)
    y = round(y, 2)
    return x, y

print(split_vector(3.1415926, 12.9999))

# %%
"""
3
Write a Python program to display a number with a comma separator.
INPUT: 
x = 3000000
y = 30000000

OUTPUT: 
Formatted Number with comma separator: 3,000,000
Formatted Number with comma separator: 30,000,000
"""

# %%
def display_number_with_comma(number: float) -> str:
    """AI is creating summary for display_number_with_comma

    Args:
        number (float): [number to add comma, for example 5000000.01]

    Returns:
        str: [str of number, with comma, for example 5,000,000.01]
    """
    return "{:,}".format(number)

print(display_number_with_comma(5000000.01))


# %%
"""
4
Write a Python program to print the following integers with zeros to the left of the specified width.
INPUT: 
x = 3
y = 123

OUTPUT: 
Formatted Number(left padding, width 2): 03
Formatted Number(left padding, width 6): 000123
"""

# %%
def add_zeros_to_int(number: int, width: int) -> str:
    """AI is creating summary for add_zeros_to_int:
    the program take number, then add zeros to long the width

    Args:
        number (int): [int to change]
        width (int): [width to add zeros]

    Returns:
        str: [string of number with the zeros]
    """
    return str(number).zfill(width)

print(add_zeros_to_int(123, 6))

# %%
"""
5
Write a Python program to swap commas and dots in a string.
INPUT: 
32.054,23

OUTPUT: 
32,054.23
"""

# %%
def swap_commas_and_dots(str_of_number: str) -> str:
    """AI is creating summary for swap_commas_and_dots
    for example:
        input- 32.054,23
        output- 32,054.23
    first replace ',' to garbage string, then replace '.' to ',', then replace the garbage string to '.'

    Args:
        str_of_number (str): [string to swap commas and dots]

    Returns:
        str: [String replaced]
    """
    return str_of_number.replace(',', '#$#^%$&^%*^%*&^$&*$').replace('.', ',').replace('#$#^%$&^%*^%*&^$&*$', '.')


print(swap_commas_and_dots("32.054,23"))

# %%
"""
6
Write a Python program to compute the sum of the digits in a given string.
INPUT: 
print(sum_digits_string("123abcd45"))
print(sum_digits_string("abcd1234"))

OUTPUT: 
15
10
"""

# %%
def compute_digits_in_str(string: str) -> int:
    """AI is creating summary for compute_digits_in_str
    compute sum all the digits in string.
    for example:
        input- 123abcd45
        output 15

    Args:
        string (str): [string output]

    Returns:
        int: [result compute]
    """
    set_of_digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    return sum(int(digit) for digit in string if digit in set_of_digits)

print(compute_digits_in_str("123abcd45"))
print(compute_digits_in_str("abcd1234"))



# %%
"""
7
Write a Python program to find the maximum length of consecutive 0's in a given binary string.
INPUT: 
str1 = "111000010000110"
str2 = "111000111"

OUTPUT: 
Original string:111000010000110
Maximum length of consecutive 0's: 4

Original string:111000111
Maximum length of consecutive 0's: 3
"""

# %%
def Finds_sequence_of_zeros(binary_string: str) -> int:
    """AI is creating summary for Finds_sequence_of_zeros:

    Args:
        binary_string (str): [string of binary number]

    Returns:
        int: [The longest sequence of zeros in the given string]
    """
    counter_zeros = 0
    current_sequence = 0
    for binary_number in binary_string:
        if not bool(int(binary_number)):
            current_sequence += 1
            if current_sequence > counter_zeros:
                counter_zeros = current_sequence
        else:
            current_sequence = 0
    return counter_zeros

print(Finds_sequence_of_zeros("111000010000110"))

# %%
"""
8
Write a Python program to find the smallest window that contains all characters in a given string.
INPUT: 
str1 = "asdaewsqgtwwsa"

OUTPUT: 
Original Strings: asdaewsqgtwwsa
Smallest window that contains all characters of the said string: daewsqgt
"""

# %%
def Finds_short_subarray(string: str) -> str:
    # new_string = string
    index_left = 0
    index_right = len(string) -1
    while (
        index_left != index_right
        and string[index_left] in string[index_left + 1 : index_right + 1]):
        index_left += 1
    while (
        index_left != index_right
        and string[index_right] in string[index_left : index_right - 1]):
        index_right -= 1
    return string[index_left:index_right +1]

string = "aabcababbaacc"
n = string[::-1]
print(n)
print(Finds_short_subarray(n))
new_string = ""
if len(Finds_short_subarray(string)) <= len(Finds_short_subarray(string[::-1])):
    new_string = Finds_short_subarray(string)
else:
    new_string = Finds_short_subarray(string[::-1])[::-1]


print(new_string)
print(Finds_short_subarray(string))
print(Finds_short_subarray(string[::-1]))

# %%
"""
9
Write a Python program to delete all occurrences of a specified character in a given string.
INPUT: 
str_text = "Delete all occurrences of a specified character in a given string"
ch = "a"

OUTPUT: 
Original string: Delete all occurrences of a specified character in a given string
Modified string: Delete ll occurrences of  specified character in  given string
"""

# %%
"""
10
Write a Python program to convert a hexadecimal color code to a tuple of integers corresponding to its RGB components.
Use a list comprehension in combination with int() and list slice notation to get the RGB components from the hexadecimal string.
Use tuple() to convert the resulting list to a tuple.

INPUT: 
print(hex_to_rgb("FFA501"))
print(hex_to_rgb("FFFFFF"))
print(hex_to_rgb("000000"))
print(hex_to_rgb("FF0000"))
print(hex_to_rgb("000080"))
print(hex_to_rgb("C0C0C0"))

OUTPUT: 
(255, 165, 1)
(255, 255, 255)
(0, 0, 0)
(255, 0, 0)
(0, 0, 128)
(192, 192, 192)
"""

# %%
"""
11
Write a Python program to convert the values of RGB components to a hexadecimal color code.
Create a placeholder for a zero-padded hexadecimal value using '{:02X}' and copy it three times.
Use str.format() on the resulting string to replace the placeholders with the given values.

INPUT: 
print(rgb_to_hex(255, 165, 1))
print(rgb_to_hex(255, 255, 255))
print(rgb_to_hex(0, 0, 0))
print(rgb_to_hex(0, 0, 128))
print(rgb_to_hex(192, 192, 192))

OUTPUT: 
FFA501
FFFFFF
000000
000080
C0C0C0
"""


