empty = 'empty'
def is_link(s):
    return s == empty or (len(s) == 2 and is_link(s[1]))
def link(first, rest):
    assert is_link(rest), "rest must be a linked list."
    return [first, rest]
def first(s):
    assert is_link(s), "first only applies to linked lists."
    assert s != empty, "empty linked list has no first element."
    return s[0]
def rest(s):
    assert is_link(s), "rest only applies to linked lists."
    assert s != empty, "empty linked list has no rest."
    return s[1]

"""sequence unpacking"""

new_run = ["09/01/2020", "10:00", 60, 6, 100]

date, pace, time, distance, elevation = new_run

print("Date: ", date)
print("Pace: ", pace, 'min')
print("Time: ", time, 'min')
print("Distance: ", distance, 'miles')
print("Elevation: ", elevation, 'feet')

# """Example of Fib sequence"""
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

# Lab 02 - Q2

def cake():
    print('beets')
    def pie():
        print('sweets')
        return 'cake'
    return pie

chocolate = cake()

more_chocolate, more_cake = chocolate(), cake

def snake(x, y):
    if cake == more_cake:
        return chocolate
    else:
        return x + y

snake(10, 20)


# Q6: Pascal's Triangle
def pascal(row, column):
    if column == 0 or row == 0:
        return 1
    else:
        return pascal()
    
# # """Q7: Double Eights"""
def double_eights(n):
    n, total = n
    def helper(n):
        if n == 0:
            return 0
        if n % 10 == 8:
            return (n // 10)
    helper(n)