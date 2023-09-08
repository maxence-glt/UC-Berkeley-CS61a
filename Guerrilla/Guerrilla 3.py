# Guerilla 3 of UC Berkeley's cs61a spring 2020 course
# https://inst.eecs.berkeley.edu/~cs61a/sp20/disc/guer03.pdf





# Link structure
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

# 1.1
# A data structure that has nested lists, one in a another recursively

# 1.3
def has_cycle(link):
    past_obj = set()
    def helper(link):
        if link.first in past_obj:
            return True
        else:
            past_obj.add(link.first)
            helper(link.rest)
    return has_cycle(link)

s = Link(1, Link(2, Link(3)))
s.rest.rest.rest = s
# has_cycle(s)





# 1.4
def seq_in_link(link, sub_link):
    link_list, sub_link_list = [], []
    def helper(link, list):
        if link is Link.empty:
            return
        list.append(link.first)
        helper(link.rest, list)
    helper(link, link_list)
    helper(sub_link, sub_link_list)
    def fast_overlap(s, t):
        i, j, count = 0, 0, 0
        print(s, t)
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                count, i, j = count + 1, i + 1, j + 1
            elif s[i] < t[j]:
                i += 1
            else:
                j += 1
        return count
    if fast_overlap(link_list, sub_link_list) == min(len(link_list), len(sub_link_list)):
        return True
    return False

lnk1 = Link(1, Link(2, Link(3, Link(4))))
lnk2 = Link(1, Link(3))
lnk3 = Link(4, Link(3, Link(2, Link(1))))
# print(seq_in_link(lnk1, lnk3))





# 2.1
# A class is an ADT with additional properties


# 2.2
# blueprint for creating objects


# 2.3
# A class atribute is an attribute shared among all objects of that class
# An instance attribute is an attribute specific to an object



    

# 2.6
class Cat():
    noise = 'meow'
    def __init__(self, name):
        self.name = name
        self.hungry = True

    def meow(self):
        if self.hungry:
            print(f"{self.noise}, {self.name} is hungry")
        else:
            print(f"Meow, my name is {self.name}")
    
    def eat(self):
        print(self.noise)
        self.hungry = False

class Kitten(Cat):
    noise = "im baby"
    def __init__(self, name, mother):
        Cat.__init__(self, name)
        self.mother = mother

    def meow(self):
        Cat.meow(self)
        print("i want mother " + self.mother.name)
        
cat = Cat('Tuna')
kitten = Kitten('Fish', cat)

cat.meow()
kitten.meow()
cat.eat()
cat.meow()
kitten.eat()
kitten.meow()