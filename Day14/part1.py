reindeers={}
fastest_reineer=""
distance=0


def travel(seconds):
    dist={}
    index={}
    points={}
    tmp=0

    for r in reindeers:
        dist[r]=0
        index[r]=0
        points[r]=0

    for i in range(seconds):
        for r in reindeers:
            index[r]=i%len(reindeers[r])
            dist[r]+=reindeers[r][index[r]]
        for r in reindeers:
            if dist[r]>tmp:
                tmp=dist[r]
                tmpr=r
        points[tmpr]+=1

    return {'dist':dist,'points':points}

with open('input.txt') as f:
    lines=f.readlines()

for line in lines:
    line=line.replace(".","")
    tokens=line.split()

    if tokens[0] not in reindeers:
        reindeers[tokens[0]]=[]

    for i in range(int(tokens[6])):
        reindeers[tokens[0]].append(int(tokens[3]))

    for i in range(int(tokens[13])):
        reindeers[tokens[0]].append(0)

res=travel(2503)

print("The longest distance={}".format(res['dist']))
print("The highest sum of points={}".format(res['points']))

