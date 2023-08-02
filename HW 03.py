# HW03 of UC Berkeley's cs61a spring 2020 course
# https://inst.eecs.berkeley.edu/~cs61a/sp20/hw/hw03/

# Q1: Num sevens
def num_sevens(x):
    if x == 0:
        return 0
    if x % 10 == 7:
        return num_sevens(x // 10) + 1
    else:
        return num_sevens(x // 10)
    
# Q2: Ping-pong
def pingpong(n):
    i = 1
    def helper(n, i, z):
        if n == z:
            return 0
        if (num_sevens(z) > 0) or (z % 7 == 0 and z != 0):
            return i * -1 + helper (n, i * -1, z + 1)
        else: 
            return i + helper(n, i, z + 1)
    def num_sevens(x):
        if x == 0:
            return 0
        if x % 10 == 7:
            return num_sevens(x // 10) + 1
        else:
            return num_sevens(x // 10)
    return helper(n, i, 0)

# Q3: Count change
def count_change(total, cents):
    if total == 0:
        return 1
    elif total < 0:
        return 0
    elif cents > total:
        return 0
    else: 
        return count_change(total, cents * 2) + count_change(total - cents, cents)

# Cool way to visualize this that I found (https://www.recursionvisualizer.com/?function_definition=def%20count_change%28total%2C%20cents%29%3A%0A%20%20%20%20if%20total%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20return%201%0A%20%20%20%20elif%20total%20%3C%200%3A%0A%20%20%20%20%20%20%20%20return%200%0A%20%20%20%20elif%20cents%20%3E%20total%3A%0A%20%20%20%20%20%20%20%20return%200%0A%20%20%20%20else%3A%20%0A%20%20%20%20%20%20%20%20return%20count_change%28total%2C%20cents%20*%202%29%20%2B%20count_change%28total%20-%20cents%2C%20cents%29&function_call=count_change%287%2C%201%29)





# Q4: Missing Digits
def missing_digits(n):
    if n < 10:
        return 0
    if ((n % 100) // 10) == ((n % 10)):
        return missing_digits(n // 10)
    if ((n % 100) // 10) != ((n % 10) - 1):
            return (((n % 10) - 1) - ((n % 100) // 10)) + missing_digits(n // 10)
    else:
        return 0