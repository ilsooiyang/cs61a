"""Coding practice for Lab 1."""

# While Loops

def factors(n):
    """Prints out all of the numbers that divide `n` evenly.

    >>> factors(20)
    20
    10
    5
    4
    2
    1
    """
    x = n
    while x > 0:
        if n % x == 0:
            print(x)
        x -= 1

    # i = 1
    # while i <= n:
    #     if n % i -- 0:
    #         print i
    #     i += 1

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 0)
    1
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    """
    total, stop = 1, n-k
    while n > stop:
        total, n = total*n, n-1
    return total
    
    # i = 1
    # n1 = n
    # if k == 0:
    #     return 1
    # elif k == 1:
    #     return n
    # else:
    #     while k > i:
    #         n *= (n1 - (k - (k - i)))
    #         i += 1
    #     return n

"""Discussion 1"""

def handle_overflow(s1, s2):
    if s1 <= 30 and s2 <= 30:
        return "No overflow"
    elif s1 > 30 and s2 < 30:
        return "%s spot(s) left in Section 2" % str(30 - s2)
    elif s1 < 30 and s2 > 30:
        return "%s spot(s) left in Section 1" % str(30 - s1)
    else:
        return "No space left in either section"

def is_prime(n):
    if n == 1:
        return False
    i = 2
    while n > i:
        if n % i == 0:
            return False
        i += 1
    return True

def fizzbuzz(n):
    i = 1
    while n >= i:
        if i % 3 == 0 and i % 5 != 0:
            print("fizz")
        elif i % 5 == 0 and i % 3 != 0:
            print("buzz")
        elif i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        else:
            print(i)
        i += 1 

def choose(n, k):
    num, den = n, k
    i = 1
    while i <= k - 1:
        num *= (n - i)
        i += 1
    i = 1
    while i <= k - 1:
        den *= (k - i)
        i += 1
    return num // den


# def keep_ints(cond, n):
#     i = 1
#     while i <= n:
#         if cond(i):
#             print(i)
#         i += 1

def keep_ints(n):
    def print_num(cond):
        i = 1
        while i <= n:
            if cond(i):
                print(i)
            i += 1
    return print_num

def is_even(x):
    return x % 2 == 0


def square(x):
    return x * x

def make_adder(x):
    def adder(n):
        return x + n
    return adder

def compose(f, g):
    def h(x):
        return f(g(x))
    return h






