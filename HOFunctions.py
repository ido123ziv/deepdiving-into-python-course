# implementation of filter
arr = [1, 2, 3, 4, 5, 6, 7, 8]
a1 = list(filter(lambda x: x > 4, arr))

# multiply by two over list
arr = [8, 5, 4, 2]
arr2 = list(map(lambda x: x*2, arr))

# get specific keys in array:
name_map_arr = [{"name" : "Ron" , "age" : 20},
       {"name" : "Dana" , "age" : 30},
       {"name" : "Gil" , "age" : 40}]

name_arr = map(lambda x: x["age"], name_map_arr)
