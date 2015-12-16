reindeers={}
fastest_reineer=""
distance=0


def travel(seconds):
    dist={}
    index={}
    points={}
    d={'deer':"",'dist':0}
    for i in range(seconds):
        for r in reindeers:
            index[r]=i%len(reindeers[r])
            if r not in dist:dist[r]=0
            dist[r]+=reindeers[r][index[r]]

        for r in reindeers:
            if dist[r]>d['dist']:
                d={"deer":r,'dist':dist[r]}
        if d['deer'] not in points:points[d['deer']]=0
        points[d['deer']]+=1
        print(dist,points)
    return dist

#with open('input.txt') as f:
with open('in.txt') as f:
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

dist=travel(140)
