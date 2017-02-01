from lab04 import *

# Q12
def flatten(lst):
    """Returns a flattened version of lst.

    >>> flatten([1, 2, 3])     # normal list
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      # deep list
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    """
    result = []
    for elem in lst:
        if type(elem) != list:
            result += [elem]
        else:
            result += flatten(elem)
    return result

# Q13
def merge(lst1, lst2):
    """Merges two sorted lists.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    lst = flatten([lst1, lst2])

    def lst_sort(lst0):
        if len(lst0) < 2:
            return lst0
        if len(lst0) == 2:
            return [min(lst0), max(lst0)]
        else:
            new_lst = lst0[:]
            new_lst.remove(min(new_lst))
            new_lst.remove(max(new_lst))
            return [min(lst0)] + lst_sort(new_lst) + [max(lst0)]

    return lst_sort(lst)
