# Lab 8 of UC Berkeley's cs61a spring 2020 course
# https://inst.eecs.berkeley.edu/~cs61a/sp20/lab/lab08/

# Link class
class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'





# Q1: Insert
def insert(link, value, index):
    if index == 0:
        link.rest = Link(link.first, link.rest)
        link.first = value
    elif link is Link.empty:
        raise ValueError
    else:
        return insert(link.first, value, index - 1)

link = Link(1, Link(2, Link(3)))
print(link)
insert(link, 9001, 0)
print(link)





# Q3: Subsequences
def insert_into_all(item, nested_list):
    return [[item] + x for x in nested_list]

def subseqs(s):
    if s == []:
        return []
    else:
        list = insert_into_all(1,  [[] for _ in range(len(s))])


seqs = subseqs([1, 2, 3])
print(sorted(seqs))
print(subseqs([]))

# nl = [[], [1, 2], [3]]
# print(insert_into_all(0, nl))





# Q4