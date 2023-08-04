# Lab 4 of UC Berkeley's cs61a spring 2020 course
# https://inst.eecs.berkeley.edu/~cs61a/sp20/lab/lab04/#q5

# Q1: Skip Add
def skip_add(n):
    if n == 0 or n < 0:
        return 0
    return n + skip_add(n - 2)





# Q2: Summation
def summation(n, term):
    if n == 0 or n < 0:
        return 0
    return term(n) + summation(n - 1, term)





# Q3: GCD
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)





# Q4: Insect Combinatorics
def paths(m, n):
    if m == 1 or n == 1:
        return 1
    return paths(m, n-1) + paths(m-1, n)





# Q5: Maximum Subsequence
def max_subseq(n, l):
    if l <= 0:
        return 0
    elif l == 1:
        return int(max(list(str(n))))
    else:
        return max_subseq(n, l - 1) + max_subseq(n, l - 2)


