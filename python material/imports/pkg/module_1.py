___all__ = ['a']

def foo():
    print('foo')

a = [1, 2, 3]

# print(f'a == {a}')

class Foo:
    pass

if (__name__ == '__main__'):
    foo()
    print(a)
    x = Foo
    print(x)