from ucb import trace

##########
# disc 4 #
##########

def rotate(lst, k):
	for _ in range(k):
		lst = [lst[-1]] + lst[0:-1]
	return lst

def replace_all_deep(d, x, y):
	lst = []
	for key in d.keys():
		if type(d[key]) == dict or d[key] == x: #if value is dict/x
			lst.append(key)
	for key in lst:
		if type(d[key]) == dict:
			replace_all_deep(d[key], x, y)
		else:
			d[key] = y
	return d

def remove_all(dict, x):
	lst = []
	for key in dict.keys():
		if dict[key] == x:
			lst.append(key)
	for key in lst:
		del dict[key]
	return dict

def add_this_many(x, el, lst):
	for _ in range(x):
	    lst.append(el)
	return lst

######################
# nonlocal statement #
######################

def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return "Insufficient funds"
        balance -= amount
        return balance
    def deposit(amount):
        nonlocal balance
        balance += amount
        return balance
    def see_balance():
        return balance
    return withdraw, deposit, see_balance



########
# tree #
########

def tree(root, branches=[]):
	for branch in branches:
		assert is_tree(branch), "branches must be trees"
	return [root] + list(branches)

def root(tree):
	return tree[0]

def branches(tree):
	return tree[1:]

def is_tree(tree):
	if type(tree) != list or len(tree) < 1:
		return False
	for b in branches(tree):
		if not is_tree(b):
			return False
	return True

def is_leaf(tree):
	return not branches(tree)

def square_tree(t):
	assert is_tree(t), "has to be a tree"
	if is_leaf(t):
		return tree(pow(root(t), 2))
	else:
		return tree(pow(root(t), 2), [square_tree(b) for b in branches(t)])
		
def height(t):
	if is_leaf(t):
		return 0
	else:
		return 1 + height(max(branches(t), key=lambda b: len(b)))

def tree_size(t):
	if is_leaf(t):
		return 1
	else:
		return 1 + sum([tree_size(b) for b in branches(t)])

def tree_max(t):
	if is_leaf(t):
		return root(t)
	else:
		return max([root(t)] + [tree_max(b) for b in branches(t)])

def leaves(t):
	if is_leaf(t):
		return t
	else:
		return [root(t)] + sum([leaves(b) for b in branches(t)], [])

def has_node(t, x):
	return x in leaves(t)

def find_path(t, x):
	if not has_node(t, x):
		return None
	if is_leaf(t):
		return t
	else:
		return [root(t)] + sum([find_path(b, x) for b in branches(t) if has_node(b, x)], [])
	#sum peels one layer of list

def hailstone_tree(n, h):
	if h == 0:
		return [n]
	elif n not in [1, 4] and (n - 1) % 3 == 0:
		return tree(n, [hailstone_tree(n * 2, h - 1), hailstone_tree((n - 1) // 3, h - 1)])
	else:
		return tree(n, [hailstone_tree(n * 2, h - 1)])
