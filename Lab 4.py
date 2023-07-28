"""Q1: Skip Add"""
def skip_add(n):
    if n == 0 or n < 0:
        return 0
    return n + skip_add(n - 2)

"""Q2: Summation"""
def summation(n, term):
    if n == 0 or n < 0:
        return 0
    return term(n) + summation(n - 1, term)

"""Q3: GCD"""
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

"""Q4: Insect Combinatorics"""
def paths(m, n):
    if m == 1 or n == 1:
        return 1
    return paths(m, n-1) + paths(m-1, n)

"""Q5: Maximum Subsequence"""
def max_subseq(n, l):
    return 

"""Q6: Pascal's Triangle"""
def pascal(row, column):
    if column == 0 or row == 0:
        return 1
    else:
        return pascal()
    
"""Q7: Double Eights"""
def double_eights(n):
    n, total = n
    def helper(n):
        if n == 0:
            return 0
        if n % 10 == 8:
            return (n // 10)
    helper(n)