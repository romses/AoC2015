maxlen=0
minlen=0

with open('input.txt') as f:
    lines=f.readlines()


for line in lines:
    line=line.strip()
    maxlen+=len(line)
    minlen+=len(eval(line))


print ("Raw len = {}".format(maxlen))
print ("Parsed len = {}".format(minlen))
print ("Difference = {}".format(maxlen-minlen))
