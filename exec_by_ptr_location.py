def add(n1=2, n2=3):
    return n1 + n2


def sub(n1=2, n2=3):
    return n1 - n2


def mul(n1=2, n2=3):
    return n1 * n2


def exec_func(f, n1, n2):
    print(f"my name is {f}\tn1: {n1}\tn2: {n2}")
    print(f(n1, n2))


def pubsub(n1, n2, ptr=[add, sub, mul]):
    for i in ptr:
        print(f"{i}, res: {i(n1, n2)}")


pubsub(3, 4)
for func in [add, sub, mul]:
    exec_func(func, 10, 13)