import math

#ex1
class CountMe: # this class count how math objects from type this class
    count = 0
    def __new__(cls):
        cls.count += 1

    @classmethod
    def how_much(cls):
        return cls.count
def task1() -> None: #counter of objects from type CountMe
    a = CountMe()
    b = CountMe()
    c = CountMe()
    d = CountMe()
    print(CountMe.how_much()) # result need to be 4
    print(CountMe.count) # result need to be 4
        
#ex2
class Vector: # class of vector (x, y) at a two-dimensional space
    
    def __init__(self, x: float = 0, y: float = 0) -> None: # constructor of Vector, take x & y so setter the data members
        assert type(x) in [int, float] and type(y) in [int, float], f"{x} and {y} need to be numbers"
        self.__x = x
        self.__y = y

    def __repr__(self) -> str: # print data of Vector wen user pass this object to print
        return f"x of vector = {self.__x}, y of vector = {self.__y}, the distance of vector from point (0,0) is {self.get_distance_of_vector()}"

    def __lt__(self, other: object) -> bool: # boolean operator, return if self smaller or biger than other or not
        return self.get_distance_of_vector() < other.get_distance_of_vector()

    def __eq__(self, other: object) -> bool: # boolean operator, return if self equal to other or not
        return self.getter() == other.getter()

    def __ne__(self, other: object) -> bool: # boolean operator, return if self not equal to other, or not
        return self.getter() != other.getter()

    def __add__(self, other: object) -> object: # operator, return vector with data of self + other
        get_other = other.getter()
        return Vector(self.__x + get_other[0], self.__y + get_other[1])

    def __sub__(self, other: object) -> object: # operator, return vector with data of self - other
        get_other = other.getter()
        return Vector(self.__x - get_other[0], self.__y - get_other[1])

    def __mul__(self, other: object) -> object:  # operator, return vector with data of self * other
        get_other = other.getter()
        return Vector(self.__x * get_other[0], self.__y * get_other[1])

    def __iadd__(self, other: object) -> object: # assignment operator, assignment self data to self data + other
        get_other = other.getter()
        self.__x += get_other[0]
        self.__y += get_other[1]
        return self

    def __isub__(self, other: object) -> object: # assignment operator, assignment self data to self data - other
        get_other = other.getter()
        self.__x -= get_other[0]
        self.__y -= get_other[1]
        return self

    def __imul__(self, other: object) -> object: # assignment operator, assignment self data to self data * other
        get_other = other.getter()
        self.__x *= get_other[0]
        self.__y *= get_other[1]
        return self

    
    def get_distance_of_vector(self) -> float: # return the distance between point (0, 0) to point of self
        return math.sqrt(self.__x ** 2 + self.__y ** 2)

    @classmethod
    def make_vec(cls, n):  # make new Vector, with x & y equal n
        return Vector(n, n)

    def getter(self) -> list: # return list of self x & y, [x, y]
        return [self.__x, self.__y]

    def setter(self, x, y) -> None: # set the data of Vector, take x & y.
        assert type(x) in [int, float] and type(y) in [int, float], f"{x} and {y} need to be numbers"
        self.__x = x
        self.__y = y


def task2() -> None:
    a = Vector(5, 3)
    b = Vector(6, 6)
    c = Vector(5, 3)
    d = Vector.make_vec(100)
    e = Vector(4)
    print(a)
    print(b)
    print(d)
    print(a < b)
    print(a > b)
    print(a == b)
    print(a == c)
    print(a != b)
    a *= b
    print(a.getter())
    a.setter(10, 2)
    print(a.getter())



def main():
    """
    task1()"""
    task2()




if __name__ == "__main__":
    main()

# 