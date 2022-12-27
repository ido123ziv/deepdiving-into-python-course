with open('names.txt', 'r') as fp:
    names = fp.readlines()
    parse = list(map(lambda x: x.split('\n')[0], names))
with open('unique_names.txt', 'w') as fp:
    for name in list(set(parse)):
        fp.writelines(name + '\n')

