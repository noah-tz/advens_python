# ex1
def ex1(a, b):
    for i in range(a, b+1):
        print(i)

def ex2(a):
    return sum(i for i in range(a) if i % 3 == 0 or i % 5 == 0)

def ex3(n):
    return 1 if n <= 1 else ex3(n -1) + ex3(n -2)

def list_of_primes(n):
    list_ = [2]
    for i in range(3, int(n ** 0.5) +1, 2):
        for j in list_:
            if i % j == 0:
                break
            if j > i ** 0.5:
                list_.append(i)
                break
    return list_
def ex4(n):
    max_ = 1
    list_ = list_of_primes(n)
    for i in list_:
        if n % i == 0:
            max_ = i
    return max_
    
    


def main():
    a = 1

    """
    ex1(10, 20)
    print(ex2(10))
    print(ex3(5))
    print(ex4(600851475143))
    print(root_abs_number(-10))"""


if __name__ == '__main__':
    main()


def calculate():
    j1 = 1
    j2 = 2
    j3 = 3
    j4 = 4
    j5 = 5
    j6 = 6
    j7 = 7

    # w1 = True
    # w2 = True
    # w3 = True
    # w4 = True
    # w5 = True
    # w6 = True
    # w7 = True

    day = 1

    while True:
        if day % j1 == 0 and day % j2 == 0 and day % j3 == 0 and day % j4 == 0 and day % j5 == 0 and day % j6 == 0 and day % j7 == 0:
            return day
        day += 1

print(calculate())
