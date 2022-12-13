from add import *


def mul(x, y):
    mult_op = 1
    sum_op = 0
    if y < 0:
        mult_op = -1
        y = y * -1
    while y > 0:
        sum_op = add(sum_op, x)
        y -= 1
    return mult_op * sum_op

def muli(x, y):
    map(lambda x, y: x + x)


def swtich(index):
    swticher = {
        1: 'a',
        2: 'b'
    }
    return swticher.get(index)