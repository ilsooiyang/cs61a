from lab05 import *

t = tree(1, [tree(2, [tree(4), tree(5, [tree(8)])]), tree(3, [tree(6, [tree(9)]), tree(7)])])

## Extra Trees Questions ##

# Q9
def info(t, target):
    """Returns a list of all the information about the song TARGET. If the song
    cannot be found in the tree, return None.

    >>> my_account = tree('inSTRUMental', [
    ...     tree('classical', [
    ...         tree('Tchaikowsky', [
    ...             tree('Piano Concerto No. 1', [
    ...                 tree('Allegro non troppo'),
    ...                 tree('Andantino'),
    ...                 tree('Allegro con fuoco')])]),
    ...         tree('Bruch', [
    ...             tree('Violin Concerto No. 1', [
    ...                 tree('Allegro moderato'),
    ...                 tree('Adagio'),
    ...                 tree('Allegro energico')])])])])
    >>> info(my_account, 'Adagio')
    ['inSTRUMental', 'classical', 'Bruch', 'Violin Concerto No. 1', 'Adagio']
    >>> info(my_account, 'Allegro non troppo')
    ['inSTRUMental', 'classical', 'Tchaikowsky', 'Piano Concerto No. 1', 'Allegro non troppo']
    >>> info(my_account, 'Sandstorm') # Should return None, which doesn't appear in the interpreter
    """
    #####################
    ##### my answer #####
    #####################
    # def leaves(t):
    #     if is_leaf(t):
    #         return t
    #     else:
    #         return [root(t)] + sum([leaves(b) for b in branches(t)], [])

    # def has_leaf(t, target):
    #     if target in leaves(t):
    #         return True
    #     return False

    # if not has_leaf(t, target):
    #     return None
    # if is_leaf(t):
    #     return t
    # else:
    #     return [root(t)] + sum([info(b, target) for b in branches(t) if has_leaf(b, target)], [])

    #####################    
    ###### answer #######
    #####################
    if root(t) == target:
        return [target]
    elif is_leaf(t):
        return None
    else:
        for b in t[1:]:
            branch = info(b, target)
            if branch != None:
                return [root(t)] + branch

    #if None is returned in a for loop
    #then it just goes on to the next iteration without stopping.
    #return breaks the loop so as soon as non-None value is obtained
    #[root(target branch)] + [target] this cycle starts until the root is reached




