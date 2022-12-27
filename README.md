# Topics Covered
## First Lesson
* One liners
* Anonymous functions
* Default Types
* Map, Reduce, Filter
* How to use native functions
* * List, Max, Sum, Len
* Decorators
* Callback Functions     
* Sorting    
## Second Lesson
* Class and Objects
* Magic Functions
* OOP:
* * Inheritance
* * Polymorphism
* * Encapsulation

## Installation
```bash
brew install python
pip3 install virtualenv 
brew install --cask pycharm
```

## Setup
```bash
virtualenv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

## Examples Map Reduce:
```python
import functools as ft
names = ["Yoav", "Ron", "Aviva", "Ronen", "Dan", "Galit"]
a1 = ft.reduce(lambda x, y: x + y, 
               map(lambda x: len(x), 
                   list(
                        filter(
                            lambda x: len(x) > 4, names)
                        )
                   )
               )
```
Will print the sum of words that are longer than 4 chars in the `name` list.

## Example Magic Functions:
How can we check if a person is greater than another ?
```python
class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
        
    def __gt__(self, other):
        return self.age > other.age

p1 = Person("ido",5)
p2 = Person("ziv",15)
print(p1 > p2)
```
## How to sort a dictionary by key?
```json
[
    {
        "name": "ido",
        "age": 35
    },
    {
        "name": "do",
        "age": 16
    },
    {
        "name": "io",
        "age": 41
    },
    {
        "name": "student_id",
        "age": 5
    }
]
```
We need to sort by key:

```python
import json
with open('people.json', 'r') as fp:
    people = json.load(fp)
people.sort(key=lambda x: x["age"])
```
We get:
```json
[
  {
    "name": "student_id",
    "age": 5
  },
  {
    "name": "ido",
    "age": 15
  },
  {
    "name": "do",
    "age": 16
  },
  {
    "name": "io",
    "age": 41
  }
]

```
