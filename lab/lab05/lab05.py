from ucb import trace

## Trees ##
# Q4
def make_pytunes(username):
    """Return a pyTunes tree as shown in the diagram with USERNAME as the value
    of the root.

    >>> pytunes = make_pytunes('i_love_music')
    >>> print_tree(pytunes)
    i_love_music
      pop
        justin bieber
          single
            what do you mean?
        2015 pop mashup
      trance
        darude
          sandstorm
    """
    return tree(username, [tree('pop', [tree('justin bieber', [tree('single', 
        [tree('what do you mean?')])]), tree('2015 pop mashup')]), 
    tree('trance', [tree('darude', [tree('sandstorm')])])])


# Q5
def num_songs(t):
    """Return the number of songs in the pyTunes tree, t.

    >>> pytunes = make_pytunes('i_love_music')
    >>> num_songs(pytunes)
    3
    """
    #song is a leaf
    #so find all leaves

    if is_leaf(t):
        return 1
    else:
        return sum([num_songs(b) for b in branches(t)])

# Q6
def find(t, target):
    """Returns True if t contains a node with the value TARGET and False
    otherwise.

    >>> my_account = tree('kpop_king',
    ...                    [tree('korean',
    ...                          [tree('gangnam style'),
    ...                           tree('wedding dress')]),
    ...                     tree('pop',
    ...                           [tree('t-swift',
    ...                                [tree('blank space')]),
    ...                            tree('uptown funk'),
    ...                            tree('see you again')])])
    >>> find(my_account, 'korean')
    True
    >>> find(my_account, 'blank space')
    True
    >>> find(my_account, 'bad blood')
    False
    """
    if root(t) == target:
        return True
    if is_leaf(t):
        return False
    else:
        for b in branches(t):
            if find(b, target):
                return True
    return False

# Q7
# @trace
def add_song(t, song, category):
    """Returns a new tree with SONG added to CATEGORY. Assume the CATEGORY
    already exists.

    >>> indie_tunes = tree('indie_tunes', [tree('indie', [tree('vance joy', [tree('riptide')])])])
    >>> new_indie = add_song(indie_tunes, 'georgia', 'vance joy')
    >>> print_tree(new_indie)
    indie_tunes
      indie
        vance joy
          riptide
          georgia

    """
    if root(t) == category:
        t = tree(root(t), branches(t) + [tree(song)])
        # t[1:] = branches(t) + [[song]]
    else:
        for b in branches(t):
            b[:] = add_song(b, song, category)
    return t

# Q8
# @trace
def delete(t, target):
    """Returns the tree that results from deleting TARGET from t. If TARGET is
    a category, delete everything inside of it.

    >>> my_account = tree('kpop_king',
    ...                    [tree('korean',
    ...                          [tree('gangnam style'),
    ...                           tree('wedding dress')]),
    ...                     tree('pop',
    ...                           [tree('t-swift',
    ...                                [tree('blank space')]),
    ...                            tree('uptown funk'),
    ...                            tree('see you again')])])
    >>> new = delete(my_account, 'pop')
    >>> print_tree(new)
    kpop_king
      korean
        gangnam style
        wedding dress
    """

    kept_branches = []
    for b in branches(t):
        if root(b) != target:
            kept_branches += [delete(b, target)]
    return tree(root(t), kept_branches)

    # if root(t) == target:
    #     t[:] = []
    #     return t
    # else:
    #     new_branches = [delete(b, target) for b in branches(t)]
    #     new_branches = [b for b in new_branches if b]
    #     return tree(root(t), new_branches)


# ADT
def tree(root, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [root] + list(branches)


def root(tree):
    return tree[0]


def branches(tree):
    return tree[1:]


def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    return not branches(tree)

numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(root(t)))
    for branch in branches(t):
        print_tree(branch, indent + 1)

