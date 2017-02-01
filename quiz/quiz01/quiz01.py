from math import ceil

def diff(x, y, z):
    """Return whether one argument is the difference between the other two.

    x, y, and z are all integers.

    >>> diff(5, 3, 2) # 5 - 3 is 2
    True
    >>> diff(2, 3, 5) # 5 - 3 is 2
    True
    >>> diff(2, 5, 3) # 5 - 3 is 2
    True
    >>> diff(-2, 3, 5) # 3 - 5 is -2
    True
    >>> diff(-5, -3, -2) # -5 - -2 is -3
    True
    >>> diff(-2, 3, -5) # -2 - 3 is -5
    True
    >>> diff(2, 3, -5)
    False
    >>> diff(10, 6, 4)
    True
    >>> diff(10, 6, 3)
    False
    """
    def a_minus_b_is_c(a, b, c):
        return a - b == c

    if a_minus_b_is_c(x, y, z) or a_minus_b_is_c(y, x, z) or a_minus_b_is_c(y, z, x) or \
       a_minus_b_is_c(z, y, x) or a_minus_b_is_c(x, z, y) or a_minus_b_is_c(z, x, y):
        return True
    else:
        return False

def abundant(n):
    """Print all ways of forming positive integer n by multiplying two positive
    integers together, ordered by the first term. Then, return whether the sum
    of the proper divisors of n is greater than n.

    A proper divisor of n evenly divides n but is less than n.

    >>> abundant(12) # 1 + 2 + 3 + 4 + 6 is 16, which is larger than 12
    1 * 12
    2 * 6
    3 * 4
    True
    >>> abundant(14) # 1 + 2 + 7 is 10, which is not larger than 14
    1 * 14
    2 * 7
    False
    >>> abundant(16)
    1 * 16
    2 * 8
    4 * 4
    False
    >>> abundant(20)
    1 * 20
    2 * 10
    4 * 5
    True
    >>> abundant(22)
    1 * 22
    2 * 11
    False
    >>> r = abundant(24)
    1 * 24
    2 * 12
    3 * 8
    4 * 6
    >>> r
    True
    """
    def find_factors(n):
        factors = []
        for i in range(1,n+1):
            if n % i == 0:
                factors.append(i)
        return factors

    def find_sum(factors):
        factors.pop()
        total = 0
        for i in factors:
            total += i
        return total

    factors = find_factors(n)
    length = len(factors)
    index = 0

    while index <= ceil(length/2) - 1:
        if length % 2 != 0 and index == length // 2:
            print(factors[index],'*',factors[index])
        else:
            print(factors[index],'*',factors[length-index-1])
        index += 1

    if find_sum(factors) > n:
        return True
    else:
        return False

def amicable(n):
    """Return the smallest amicable number greater than positive integer n.

    Every amicable number x has a buddy y different from x, such that
    the sum of the proper divisors of x equals y, and
    the sum of the proper divisors of y equals x.

    For example, 220 and 284 are both amicable because
    1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110 is 284, and
    1 + 2 + 4 + 71 + 142 is 220

    >>> amicable(5)
    220
    >>> amicable(220)
    284
    >>> amicable(284)
    1184
    >>> r = amicable(5000)
    >>> r
    5020
    """
    def find_factors(n): #find_factors(220) => [1,2,4,5,10,11,20,22,44,55,110]
        factors = []
        for i in range(1,n+1):
            if n % i == 0:
                factors.append(i)
        return factors

    def find_sum(factors): #find_sum(find_factors(220)) => 284
        factors.pop()
        total = 0
        for i in factors:
            total += i
        return total

        
    def num_is_amicable(n):
        pair = find_sum(find_factors(n)) #284
        if n != pair and find_sum(find_factors(pair)) == n:
            return True
        else:
            return False
    
    pair = find_sum(find_factors(n)) #284
    n_copy = n
    if num_is_amicable(n) and n < pair:
        return pair
    else:
        while True:
            pair = find_sum(find_factors(n_copy))
            if num_is_amicable(n_copy) and n_copy > n:
                return n_copy
            else:
                n_copy += 1



















