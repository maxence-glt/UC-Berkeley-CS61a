# Guerilla 01 of UC Berkeley's cs61a spring 2020 course
# https://inst.eecs.berkeley.edu/~cs61a/sp20/disc/guer01.pdf

# 1.3
def map_mut(f, L):
    for x in L: 
        L[x-1] = f(x)
    




# 1.10
def paths(m, n):
    if m == 1 or n == 1:
        return 1
    elif m == 0 or n == 0:
        return 0
    else:
        return paths(m-1, n) + paths(m, n-1)
    
#1.11
def merge(s1, s2):
    if s1 == [] or s2 == []:
        return s1 + s2
    elif s1[0] < s2[0]:
        return s1[:1] + merge(s1[1:], s2)
    elif s1[0] > s2[0]:
        return s2[:1] + merge(s1, s2[1:])

#1.12
def mario_number(level):
    length = len(level)
    def helper(level, length):
        if length == 1 or length == 2:
            return 1
        if level[1] == "P" and level[2] == "P":
            return False
        if level[0] == "-" and level[1] == "-" and level[2] == "-":
            return helper(level[1:], length - 1) + helper(level[2:], length - 2)
        if level[1] == "-":
            return helper(level[1:], length - 1)
        if level[1] == "P":
            return helper(level[2:], length - 2)
    if helper(level, length) == 0:
        return 0
    else:
        return helper(level, length)