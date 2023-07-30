# Discussion 1 of UC Berkeley's cs61a spring 2020 course
# https://inst.eecs.berkeley.edu/~cs61a/sp20/disc/disc01.pdf

# 1.1
def wears_jacket_with_if(temp, raining):
    if temp <= 60 or raining == True:
        return True
    else:
        return False
    
def wears_jacket(temp, raining):
    return True if ((temp <= 60) or (raining == True)) else False





# 1.3
def is_prime(n):
    index = n - 1
    True
    while index != 1:
        if n % index == 0:
            index = 1
            return False
        else:
            index -= 1
            return True
