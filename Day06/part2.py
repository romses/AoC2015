garden=[[0 for i in xrange(1000)] for i in xrange(1000)]
burning_lights=0


def lightswitch(line):
    line=line.strip()
    tokens=line.split()

    if len(tokens)==5: del tokens[0]

    x1,y1=tokens[1].split(",")
    x2,y2=tokens[3].split(",")

    action=tokens[0]

    x1=int(x1)
    x2=int(x2)+1
    y1=int(y1)
    y2=int(y2)+1
    for x in range(x1,x2):
        for y in range(y1,y2):
            if action=="on":
                garden[x][y]+=1
            if action=="off":
                if garden[x][y]>0:
                    garden[x][y]-=1
            if action=="toggle":
                garden[x][y]+=2

def count():
    burning_lights=0
    for x in range(0,1000):
        for y in range(0,1000):
            burning_lights+=garden[x][y]
    return burning_lights

with open('input.txt') as f:
    lines=f.readlines()

for line in lines:
    lightswitch(line)


print("Santa told you to lit yout lights with a total of  {} lumen".format(count()))

