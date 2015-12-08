import json

maxlen=0
newlen=0

with open('input.txt') as f:
    lines=f.readlines()


for line in lines:
    line=line.strip()
    maxlen+=len(line)
    newlen+=len(json.dumps(line)) - len(line)


print ("Raw len = {}".format(maxlen))
print ("New len = {}".format(newlen))
