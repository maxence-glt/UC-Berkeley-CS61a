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





# Q3: Distance
from math import sqrt

def make_city(name, lat, lon):
    return [name, lat, lon]

def get_name(city):
    return city[0]

def get_lat(city):
    return city[1]

def get_lon(city):
    return city[2]

def distance(city1, city2):
    lat1, lon1 = city1[1], city1[2]
    lat2, lon2 = city2[1], city2[2]
    return sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2)





# Q4: Closer city
def closer_city(lat, lon, city1, city2):
    lat1, lon1 = get_lat(city1), get_lon(city1)
    lat2, lon2 = get_lat(city2), get_lat(city2)
    if abs(sqrt((lat1 - lat)**2 + (lon1 - lon)**2)) < abs(sqrt((lat2 - lat)**2 + (lon2 - lon)**2)):
        return get_name(city1)
    else:
        return get_name(city2)





# Q6: Nut Finder
def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def nut_finder(t):
    for x in t:
        if label(x) == "nut":
            return True
        if is_leaf(t) == True:
            return False
        else:
            return nut_finder(branches(t))
    
