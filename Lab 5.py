# Lab 5 of UC Berkeley's cs61a spring 2020 course
# https://inst.eecs.berkeley.edu/~cs61a/sp20/lab/lab05/

# Q1: List Indexing
x = [1, 3, [5, 7], 9]
x[2, 1]

x = [[3, [5, 7], 9]]
x[0][1][1]





# Q2: Couple
def couple(lst1, lst2):
    assert len(lst1) == len(lst2)
    return [lst1[i:i + 1] + lst2[i:i + 1] for i in range(len(lst1))]





