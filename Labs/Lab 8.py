# Lab 8 of UC Berkeley's cs61a spring 2020 course
# https://inst.eecs.berkeley.edu/~cs61a/sp20/lab/lab08/

# Link class
class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'





# Q1: Insert
def insert(link, value, index):
    if index == 0:
        link.rest = Link(link.first, link.rest)
        link.first = value
    elif link is Link.empty:
        raise ValueError
    else:
        return insert(link.first, value, index - 1)

link = Link(1, Link(2, Link(3)))
print(link)
insert(link, 9001, 0)
print(link)





# Q3: Subsequences
def insert_into_all(item, nested_list):
    return [[item] + x for x in nested_list]


# attempt 1
def subseqs(s):
    if s == []:
        return [[]]
    else:
        num = [[s[0]] + [x] for x in s[1:]]
        return [[s[0]]] + num + subseqs(s[1:])


# attempt 2 (correct)
def subseqs(s):
    if s == []:
        return [[]]
    else:
        num = [[s[0]] + x for x in subseqs(s[1:])]
        return num + subseqs(s[1:])

# THIS ONE TOOK ME FOREVER





# Q4: Increasing Subsequences
def inc_subseqs(s):
    def subseq_helper(s, prev):
        if not s:
            return [[]]
        
        elif s[0] < prev: 
            return 

    return subseq_helper(s, )





# Q5: Generate Permutations
def permutations(seq):
    if len(seq) <= 1:
        yield seq
    else:
        for perm in seq:
            for num in range(len(seq)):
                permutations([perm] + [seq[num]])





# Q6: Keyboard
class Button:
    def __init__(self, pos, key):
        self.pos = pos
        self.key = key
        self.times_pressed = 0

class Keyboard:
    def __init__(self, *args):
        self.buttons = {}
        for key in args:
            self.buttons[key.pos] = key
    
    def press(self, info):
        if info > len(self.buttons) - 1:
            return "''"
        self.buttons[info].times_pressed += 1
        return self.buttons[info].key
    
    def typing(self, typing_input):
        out = ""
        for index in typing_input:
            out += Keyboard.press(self, index)
        return out




# Q7: Advanced Counter
def make_advanced_counter_maker():
    global_count = 0
    def make_counter():
        specific_count = 0
        def specific_counter(identifier):
            nonlocal global_count
            nonlocal specific_count
            if identifier == "count":
                specific_count += 1
                return specific_count
            if identifier == "reset":
                specific_count = 0
                return
            if identifier == "global-count":
                global_count += 1
                return global_count
            if identifier == "global-reset":
                global_count = 0
                return
        return specific_counter
    return make_counter





# Q8: Trade
# def trade(first, second):
    # m, n = 1, 1

    # equal_prefix = lambda: first == second
    # while :
    #     if :
    #         m += 1
    #     else:
    #         n += 1

    # if equal_prefix():
    #     first[:m], second[:n] = second[:n], first[:m]
    #     return 'Deal!'
    # else:
    #     return 'No deal!'

a = [1, 1, 3, 2, 1, 1, 4]
b = [4, 3, 2, 7]
trade(a, b)
print(a)
print(b)





# Q10: Deep Linked List Length
def deep_len(lnk):
    if lnk.first.rest is not Link.empty:
        return 0
    elif lnk.rest is Link.empty:
        return 1
    else: 
        return sum([1 for x in lnk.first]) + deep_len(lnk.rest)
