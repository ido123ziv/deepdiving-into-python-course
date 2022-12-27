import json

import requests
url = "https://jsonplaceholder.typicode.com/users/"
user = input("Please enter your id:\n")
url_todo = 'https://jsonplaceholder.typicode.com/todos'
params = {'user': int(user)}
print(params)
res = requests.get(url+user)
try:
    response_json = res.json()
    with open('result.json', 'w') as fp:
        json.dump(response_json, fp, indent=4)
    name = response_json['name']
    print(f"name: {name}, email: {response_json['email']}")
    if name:
        if name[0].lower() == 'e':
            res_todo = requests.get(url_todo, params={'userId': user})
            todos = res_todo.json()
        with open('result-todo.json', 'w') as fp:
            json.dump(list(map(lambda x: x['title'], todos)), fp, indent=4)
except Exception as e:
    print("Caught an Error :( {}".format(e))

