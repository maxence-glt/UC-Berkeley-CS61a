#1.3
def map_mut(f, L):
    for x in L: 
        L[x-1] = f(x)
    
L = [1, 2, 3, 4]
map_mut(lambda x: x**2, L)
L #[1, 4, 9, 16]

#1.10
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
    i