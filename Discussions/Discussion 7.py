# Discussion 7 of UC Berkeley's cs61a spring 2020 course
# https://inst.eecs.berkeley.edu/~cs61a/sp20/disc/disc07.pdf

# 1.2
class Email:
    def __init__(self, msg, sender_name, recipient_name):
        self.msg = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name

class Server:
    def __init__(self):
        self.clients = {}

    def send(self, email):
        client = self.clients[email.recipient_name]
        client.recieve(email)

    def register_client(self, client, client_name):
        self.clients[client_name] = client

class Client:
    def __init__(self, server, name):
        self.inbox =[]
        self.server = server
        self.name = name
        self.server.register_client(self, self.name)

    def compose(self, msg, recipient_name):
        email = Email(msg, self.name, recipient_name)
        self.server.send(email)

    def recieve(self, email):
        self.inbox.append(email)





# 2.1
class Pet():
    def __init__(self, name, owner):
        self.is_alive = True # It's alive!!!
        self.name = name
        self.owner = owner

    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print(self.name)

class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        Pet.__init__(self, name, owner)
        self.lives = lives

    def talk(self):
        print(self.name + " says meow!")

    def lose_life(self):
        if self.lives == 0:
            self.is_alive = False
        if self.lives < 0:
            print("Cat has no more lives to lose")
        self.lives -= 1





# 2.2
class NoisyCat(Cat):
    def __init__(self, name, owner, lives=9):
        Cat.__init__(self, name, owner, lives)
        # unnessesary

    def talk(self):
        Cat.talk(self)
        Cat.talk(self)

NoisyCat("Magic", "James").talk()





# 2.3
class A:
    def f(self):
        return 2
    def g(self, obj, x):
        if x == 0:
            return A.f(obj)
        return obj.f() + self.g(self, x - 1)
    
class B(A):
    def f(self):
        return 4
    
x, y = A(), B()





# Linked list class
class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    # def __repr__(self):
    #     if self.rest:
    #         rest_str = ', ' + repr(self.rest)
    #     else:
    #         rest_str = ''
    #     return 'Link({0}{1})'.format(repr(self.first), rest_str)

    # def __str__(self):
    #     string = '<'
    #     while self.rest is not Link.empty:
    #         string += str(self.first) + ' '
    #         self = self.rest
    #     return string + str(self.first) + '>'
    
# 3.1
def sum_nums(lnk):
    if lnk.rest is Link.empty:
        return lnk.first
    else:
        return lnk.first + sum_nums(lnk.rest)





# 3.2
def multiply_lnks(lst_of_lnks):
    total = 1
    for x in lst_of_lnks:
        if x.rest is Link.empty:
            return Link.empty
        total *= x.first
    lst_of_lnks = [lnk.rest for lnk in lst_of_lnks]
    return Link(total, multiply_lnks(lst_of_lnks))

a = Link(2, Link(3, Link(5)))
b = Link(6, Link(4, Link(2)))
c = Link(4, Link(1, Link(0, Link(2))))
p = multiply_lnks([a, b, c])





# 3.3
def filter_link(link, f):
    while link is not Link.empty:
        if f(link.first):
            yield link.first
        link = link.rest





def filter_no_iter(link, f):
    if link is Link.empty:
        return
    elif f(link.first):
        yield link.first
    yield from (filter_no_iter(link.rest, f))
# Stuck on this one for a while, all that I had missing was the yield from!

link = Link(1, Link(2, Link(3)))
print(list(filter_no_iter(link, lambda x: x % 2 != 0)))





# 1. Midterm Review Snax
def feed(snax, x, y):
    def helper(lst, p, q):
        if p < 0 and q < 0:
            return helper(lst, p + x, q + y)
        elif p < 0:
            return helper
        elif q < 0:
            return helper
    
    return helper(snax, x, y)

# stuck on this one