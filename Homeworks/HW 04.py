# HW04 of UC Berkeley's cs61a spring 2020 course
# https://inst.eecs.berkeley.edu/~cs61a/sp20/hw/hw04/

# Q1
def mobile(left, right):
    assert is_arm(left), "left must be a arm"
    assert is_arm(right), "right must be a arm"
    return ['mobile', left, right]

def is_mobile(m):
    return type(m) == list and len(m) == 3 and m[0] == 'mobile'

def left(m):
    assert is_mobile(m), "must call left on a mobile"
    return m[1]

def right(m):
    assert is_mobile(m), "must call right on a mobile"
    return m[2]

def arm(length, mobile_or_planet):
    assert is_mobile(mobile_or_planet) or is_planet(mobile_or_planet)
    return ['arm', length, mobile_or_planet]

def is_arm(s):
    return type(s) == list and len(s) == 3 and s[0] == 'arm'

def length(s):
    assert is_arm(s), "must call length on a arm"
    return s[1]

def end(s):
    assert is_arm(s), "must call end on a arm"
    return s[2]

def planet(size):
    assert size > 0
    return ["planet", size]

def size(w):
    assert is_planet(w), 'must call size on a planet'
    return w[1]

def is_planet(w):
    return type(w) == list and len(w) == 2 and w[0] == 'planet'

def total_weight(m):
    if is_planet(m):
        return size(m)
    else:
        assert is_mobile(m), "must get total weight of a mobile or a planet"
        return total_weight(end(left(m))) + total_weight(end(right(m)))
    




# Q2: Balanced    
def balanced(m):
    if is_planet(m):
        return True
    if (total_weight(end(left(m))) * length(left(m))) != (total_weight(end(right(m))) * length(right(m))):
        return False
    if (total_weight(end(left(m))) * length(left(m))) == (total_weight(end(right(m))) * length(right(m))):
        return balanced(end(left(m))) and balanced(end(right(m)))
    else: return False





# Q3: Totals
def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
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

def print_tree(t, indent=0):
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)





def totals_tree(m):
    if is_planet(m):
        return tree(total_weight(m))
    else:
        return tree(total_weight(m), [totals_tree(end(left(m))), totals_tree(end(right(m)))])
    




# Q4: Replace leaf
def replace_leaf(t, old, replacement):
    if is_leaf(t) and label(t) == old:
        return tree(replacement)
    return tree(label(t), [])
# Stuck on this one





# Q5: Password Protected Account
def make_withdraw(balance, password):
    attempts = []
    def withdraw(amount, password2):
        nonlocal balance
        nonlocal attempts
        if len(attempts) == 3:
            return "Your account is locked. Attempts: " + str(attempts)
        elif password == password2:
            if amount > balance:
                return "Insufficient funds"
            balance = balance - amount
            return balance
        else: 
            attempts.append(password2)       
            return "Incorrect password"
    return withdraw





# Q6: Joint Account
def make_joint(withdraw, old_pass, new_pass):
    def withdraw2(amount, password):
        if password == old_pass or password == new_pass:
            return withdraw(amount, old_pass)
        return withdraw(0, password)
    if withdraw(0, old_pass) == "Incorrect password":
        return "Incorrect password"
    else: return withdraw2





# Extra Questions





# Q7: Interval Abstraction
def interval(a, b):
    return [a, b]

def lower_bound(x):
    return x[0]

def upper_bound(x):
    return x[1]

def mul_interval(x, y):
    p1 = lower_bound[x] * lower_bound[y]
    p2 = lower_bound[x] * upper_bound[y]
    p3 = upper_bound[x] * lower_bound[x]
    p4 = upper_bound[x] * upper_bound[y]
    return interval([min(p1, p2, p3, p4), max(p1, p2, p3, p4)])





# Q8: Sub Interval
def sub_interval(x, y):
    p1 = lower_bound[x] - lower_bound[y]
    p2 = lower_bound[x] - upper_bound[y]
    p3 = upper_bound[x] - lower_bound[x]
    p4 = upper_bound[x] - upper_bound[y]
    return interval([min(p1, p2, p3, p4), max(p1, p2, p3, p4)])





# Q9: Div Interval
def div_interval(x, y):
    assert lower_bound(x) > 0 and lower_bound(y) > 0, "No interval that spans 0 can be used as a divisor!"
    reciprocal_y = interval(1/upper_bound(y), 1/lower_bound(y))
    return mul_interval(x, reciprocal_y)
