# now we will work on decorators
def get_greet(f):
    def inner_function():
        f()
        print("world!")
    return inner_function


@get_greet
def print_hello():
    print("hello")


@get_greet
def print_bye():
    print("bye")


print_hello()
print_bye()

#####################################
def dect(f):
    def inner_function(num):
        print(num)
        return f(f(f(num)))
    return inner_function


def dect2(f):
    def inner_function(num):
        print(num)
        return f(num) * 4
    return inner_function


@dect
def mul(num):
    return num * 2


print(mul(4))
