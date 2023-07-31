"""Discussion"""

"""Question 1.1 - multiply"""
def multiply(m, n):
    total = 0
    if m == 0 or n == 0:
        return 0
    else:
        total = m + multiply(m, n-1)
        return total
    
"""Question 1.3 - hailstone"""
def hailstone(n):
    print(int(n))
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + hailstone(n // 2)
    else:
        return 1 + hailstone(3 * n + 1)
    
"""Question 1.4 - is_prime"""
def is_primeORIGINAL(n):
    if n == 1:
        return False
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True

def is_prime(n):
    k = 2
    return prime_helper(n, k)
    
def prime_helper(n, k):
    if n == 1:
        return False
    elif n % k == 0:
        return False  
    else: 
        (prime_helper(n, k + 1))
    return True

"""Question 1.5 - merge"""
def merge(n1, n2):
    if n1 == 0 or n2 == 0:
        return n1 + n2
    if n1 % 10 > n2  % 10:
        return n2 % 10 + (10 * n1 % 10) + (10 * merge(n1 // 10, n2 // 10))
    if n2 % 10 > n1  % 10:
        return n1 % 10 + (10 * n2 % 10) + (10 * merge(n1 // 10, n2 // 10))

    """Answer below"""        
def merge(n1, n2):
    """ 
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31) 
    3211
    """
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    elif n1 % 10 < n2 % 10:
        return merge(n1 // 10, n2) * 10 + n1 % 10
    else:
        return merge(n1, n2 // 10) * 10 + n2 % 10        
    
merge(32, 41)



