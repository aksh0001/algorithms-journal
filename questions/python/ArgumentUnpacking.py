"""
What does the "*" and "**" do?

1) Regular multiplication and power operations
2) Extending list-type containers
3) Unpacking containers
4) Variadic Arguments

https://medium.com/understand-the-python/understanding-the-asterisk-of-python-8b9daaa4a558
https://www.youtube.com/watch?v=YWY4BZi_o28

@author a.k
"""

# Use Case 1
# print('-----\n>>>U.C. 1<<<')
# a, b = 2, 5
# print(a * b, a ** b)

# Use Case 2
print('-----\n>>>U.C. 2<<<')
zeros = [0] * 4
ztup = (0,) * 4
vec = [[1, 7, 3, 8]] * 3
print(zeros, ztup)
print(vec)

# Use Case 3
print('-----\n>>>U.C. 3<<<')


def print_vector(x, y, z):
    print('<%s, %s, %s>' % (x, y, z))


print_vector(2, 1, 3)
tup = (6, 1, 9)
print_vector(*tup)  # unpack and match tup to the args (instead of print_vector(tup[0], tup[1], tup[2]))
ls = [1, 8, 3]
print_vector(*ls)  # unpack and match list to the args
dic = {'x': 8, 'y': 9, 'z': 2}
print_vector(*dic)  # unpack and match dict keys to the args
print_vector(**dic)  # unpack and match dict values to the args (dict keys must match name of args and number of args)

*ls, a = ls
print(ls, a)

# Use case 4
print('-----\n>>>U.C. 4<<<')


def variadic(*args, **kwargs):
    if args:
        print(args)
    if kwargs:
        print(kwargs)


variadic('hello', 2, 'hi', kw1='hey', kw2=99, another_kw=float('inf'))  # positional wrapped w/ tuple and keyword w/dict


def fizz_buzz(req, *args, **kwargs):
    """
    Example of a function with variadic arguments.
    :param req: required positional arguments
    :param args: collects the extra positional arguments into a tuple
    :param kwargs: collects the extra keyword arguments into a dict with K:V pairs
    :return: none
    """
    for i in range(1, req + 1):
        if args:
            if i in args:
                print('FIZZ')
                continue
        if kwargs:
            if i % 5 == 0 and 'ksi' in kwargs:
                print('>> KSI =', kwargs['ksi'])
                continue
        print(i)
    return


fizz_buzz(10, 3, 6, 7, 2, pear=1, apple=2, banan=33, ksi=44)


class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage


class BlueCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = 'blue'
