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