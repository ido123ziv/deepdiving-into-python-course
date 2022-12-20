from Person import Person
mi = {}
for i in range(5):
    mi[i] = Person(str(i), (i+1)**(i+1))

print("Who is greater: {} or {}? \n {}".format(mi[0], mi[1], mi[0] > mi[1]))
print("Let's add: {} and {}? \n {}".format(mi[2], mi[3], mi[2] + mi[3]))
print("Who is greater or equal: {} or {}? \n {}".format(mi[0], mi[4], mi[0] >= mi[4]))

