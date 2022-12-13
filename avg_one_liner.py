my_map = {
    "nums": [77, 95],
    "Student": {
        "Name": "Avi",
        "ID": 111111,
        "Grades": {

            "score": [89, 96, 100]

        }
    }
}


print(max(sum(my_map["Student"]["Grades"]["score"]) / len(my_map["Student"]["Grades"]["score"]),
          sum(my_map["nums"]) / len(my_map["nums"])))
