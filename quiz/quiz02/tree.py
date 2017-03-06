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

def leaves(tree):
    if is_leaf(tree):
        return [root(tree)]
    else:
        return [root(tree)] + sum([leaves(b) for b in branches(tree)], [])

t = tree(1, [tree(-1, [tree(2)]),
             tree(8, [tree(-7)]),
             tree(-3, [tree(-3)]),
             tree(-4, [tree(3), tree(-5), tree(7, [tree(-4), tree(-2)])])]
         )

