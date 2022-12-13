# Topics Covered
* One liners
* Anonymous functions
* Map, Reduce, Filter
* How to use native functions
* Decorators
* Callback Functions     
* Sorting    

## Installation
```bash
brew install python
pip3 install virtualenv 
brew install --cask pycharm
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

