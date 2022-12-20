import copy
arr = [10, 1, 5, 8, 1, 10, 1, 3, 9, 10]
copied_arr = copy.deepcopy(arr)
print(f"arr: {arr}")
# sort existing
copied_arr.sort()
print(f"original: {arr}, sorted arr: {copied_arr}")
# return new sorted array
arr2 = sorted(arr)
print(f"original: {arr}, sorted arr: {arr2}")
# sort reverse
copied_arr = copy.deepcopy(arr)
copied_arr.sort(reverse=True)
print(f"original: {arr}, reverse arr: {copied_arr}")
# sort by key
people = [
    {"name": "ido", "age": 15},
    {"name": "do", "age": 16},
    {"name": "io", "age": 41},
    {"name": "student_id", "age": 5}
]
people.sort(key=lambda x: x["age"])
print(people)