from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)



def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    def square(n):
        return n*n

    num = [a, b, c]
    first = max(num)
    num.remove(first)
    second = max(num)
    return square(first)+square(second)



def largest_factor(n):
    """Return the largest factor of n*n-1 that is smaller than n.

    >>> largest_factor(4) # n*n-1 is 15; factors are 1, 3, 5, 15
    3
    >>> largest_factor(9) # n*n-1 is 80; factors are 1, 2, 4, 5, 8, 10, ...
    8
    """
    "*** YOUR CODE HERE ***"
    num = n*n-1 #n=4 num=15
    factors = []
    for x in range(1, n*n): #1,2,3...15
        if num % x == 0:
            factors.append(x)
    factors = [x for x in factors if x <= n]
    return max(factors)



def with_if_statement():
    """
    >>> with_if_statement()
    1
    """
    if c():
        return t()
    else:
        return f()



def with_if_function():
    return if_function(c(), t(), f())



def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result

def c():
    return True

def t():
    return 1

def f():
    raise ValueError('A very specific bad thing happened') # or 1/0



def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    steps = 1
    print(n)
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        steps += 1
        print(n)
    return steps



def multiple(a, b):
    """Return the smallest number n that is a multiple of both a and b.

    >>> multiple(3, 4)
    12
    >>> multiple(14, 21)
    42
    """
    num = bigger = max(a, b)
    while True:
        if num % a == 0 and num % b == 0:
            break
        else:
            num += bigger
    return num


def unique_digits(n):
    """Return the number of unique digits in positive integer n

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(1313131) # 1 and 3
    2
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(10000) # 0 and 1
    2
    >>> unique_digits(101) # 0 and 1
    2
    >>> unique_digits(10) # 0 and 1
    2
    """
    numbers = list(str(n)) # e.g. ['1', '2', '1', '3']
    one_to_nine = []
    for n in list(range(10)):
        one_to_nine.append(str(n)) #['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    num_of_int = 0
    for n in one_to_nine:
        if n in numbers:
            num_of_int += 1
    return num_of_int



