# Some notes on generator functions in Python.

# https://www.programiz.com/python-programming/generator

def my_gen():
    """
    A simple generator function.
    """
    n = 1
    print('This is printed first.')
    yield n

    n += 1
    print('This is printed second.')
    yield n

    n += 1
    print('This is printed last.')
    yield n

def rev_str(my_str: str):
    """
    Reverse string using generator.
    """
    L = len(my_str)
    for i in range(L-1, -1, -1):
        yield my_str[i]

def PowTwoGen(_max: int=0):
    """
    Generator function for powers of two.
    """
    n = 0
    while n < _max:
        yield 2 ** n
        n += 1

def f(i, n):
    """
    Example of a generator function that uses recursion.
    """
    if i > n:
        yield i
    else:
        for j in range(1, n):
            for val in f(i+j, n):
                yield val
