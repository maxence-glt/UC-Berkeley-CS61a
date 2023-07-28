"""HW 02"""
def accumulate(combiner, base, n, f):
    total, k = base, 1
    while k <= n:
        total, k = combiner(total, f(k)), k + 1
    return total

"""HW 03 Make Repeater"""
def make_repeater(h, n):
    h, n 

"""Lab 02 - Q2"""

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