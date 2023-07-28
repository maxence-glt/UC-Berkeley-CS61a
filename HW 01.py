"""HW01 Q4"""
def largest_factor(x):
    n = x
    while x > 1:
        n = n -1
        if x % n == 0:
            return n

"""Q6"""
def hailstone(x):
    n = 1
    while x != 1:
        print(x)
        if ((x % 2) == 0):
            x = x / 2
        else:
            x = (x * 3) + 1
    print(x)
    return n

"""Example of Fib sequence"""
def fib(n):
    """Compute the nth Fibonacci number, for n >= 2."""
    pred, curr = 0, 1   # Fibonacci numbers 1 and 2
    k = 2               # Which Fib number is curr?
    while k < n:
        pred, curr = curr, pred + curr
        k = k + 1
    return curr

positive = -9
negative = -12
while negative:
   if positive:
       print(negative)
   positive += 3
   negative += 3

def sum_digits(x):
    length = x
    while length > 0:
        x = (x-(x-1))
        length - 1
