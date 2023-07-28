"""1.1"""
def count_stair_ways(n):
    if n == 1 or 0:
        return n
    elif n == 2: 
        return 2
    else: 
        return count_stair_ways(n - 1) + (n - 2)

"""1.2"""
def count_k(n, k):
    if k == 1 or n == 1:
        return 1
    return count_k(n, k-1) + count_k(n-1, k)

"""2.2"""
def even_weighted(s):
    return[x * s [x]for x in range(len(s)) if x % 2 == 0]

"""2.3"""
def max_product(s):
    if s == []:
        return 1
    else:
        return max(max_product(s[1:]), s[0] * max_product(s[2:]))

"""Whole Numbers"""
"""(a)"""
def check_hole_number(n):
    if n == 0:
        return 
    if n % 10 > ((n % 100) // 10):
        return bool(n) 
    else:
        return 