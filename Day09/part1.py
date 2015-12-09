nodes={}
edges={}
visited=[]

pathlen=0
minpath=32767
maxpath=0

def pathlen():
    global minpath
    global maxpath
    pathlen=0
    for i in range(len(visited)-1):
        pathlen+=int(edges[visited[i]+"-"+visited[i+1]])
    if pathlen<minpath: 
        minpath=pathlen
    if pathlen>maxpath: 
        maxpath=pathlen


def recurse():
    if(len(visited)==len(nodes)):
        pathlen()

    for v in nodes:
        if nodes[v]['visited']==0:
            nodes[v]['visited']=1
            visited.append(v)
            recurse()
            visited.pop()
            nodes[v]['visited']=0
    return 0+5


with open('input.txt') as f:
    lines=f.readlines()

for line in lines:
    tokens=line.split()

    nodes[tokens[0]]={'visited':0}
    nodes[tokens[2]]={'visited':0}

    key1=tokens[0]+"-"+tokens[2]
    key2=tokens[2]+"-"+tokens[0]

    if key1 not in edges: edges[key1]=[]
    edges[key1]=tokens[4]
    if key2 not in edges: edges[key2]=[]
    edges[key2]=tokens[4]


recurse()
print("The minimal pathlen = {}".format(minpath))
print("The maximal pathlen = {}".format(maxpath))
