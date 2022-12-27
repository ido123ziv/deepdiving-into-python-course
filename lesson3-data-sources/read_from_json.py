import json
with open('data.json', 'r') as fp:
# fp = open('data.json', 'r+')
    data = json.load(fp)

avg = sum(data['Student']['Grades']['exams']) / len(data['Student']['Grades']['exams'])
data['Student']['Grades']['avg'] = avg

with open('data.json', 'w') as fp:
    json.dump(data, fp, indent=4)
print(json.dumps(data, indent=4))
fp.close()
