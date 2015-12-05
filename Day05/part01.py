naughty=['ab','cd','pq','xy']
nice=['a','e','i','o','u']

nice_children=0

with open('input.txt') as f:
    lines=f.readlines()



for line in lines:
    vowel=0
    doublechar=False
    naughtyelement=False

    line=line.strip()
    for c in line:
        if(c in nice):
            vowel+=1
    for i in range(1,len(line)):
        if line[i-1]==line[i]:
            doublechar=True
    for n in naughty:
        if n in line:
            naughtyelement=True

    if vowel>2 and doublechar==True and naughtyelement==False:
        nice_children+=1

print("Santas list contains {} nice children".format(nice_children))
