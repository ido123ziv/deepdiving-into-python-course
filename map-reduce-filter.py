import functools as ft
# ex 1
def string_counter(word="hello"):
    return len(word)


arr = ["ido", "ziv", "123"]
print(sum(map(lambda x: string_counter(x), arr)))

arr_num = map(lambda x: string_counter(x), arr)
print(ft.reduce(lambda x, y: x + y, arr_num))
# def array_of_string_counter(arr):
#     sum_arr = 0
#     for i in arr:
#         sum_arr += string_counter(i)
#     print(sum_arr)

# def array_filter(my_arr):
# array_of_string_counter(arr)
# ex2
names = ["Yoav", "Ron", "Aviva", "Ronen", "Dan", "Galit"]
# a1 = sum(map(lambda x: len(x), list(filter(lambda x: len(x) > 4, names))))
a1 = ft.reduce(lambda x, y: x + y, map(lambda x: len(x), list(filter(lambda x: len(x) > 4, names))))
print(a1)

# ex 4
int_arr = [6, 2, 8, 12, 4]
my_min = ft.reduce(lambda x, y: min(x,y), int_arr)
print(my_min)
