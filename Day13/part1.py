guests={}
likehood={}
visited=[]
happyness=0

def pathlen():
    global happyness
    tmphappy=0
    for x in range(len(visited)):
        y=x+1
        if y == len(visited):y=0
        tmphappy+=likehood[visited[x]][visited[y]]
        tmphappy+=likehood[visited[y]][visited[x]]

    if(tmphappy>happyness):
        happyness=tmphappy
        print(visited[x],visited[y],likehood[visited[x]][visited[y]])

    print("\n")

def recurse():
    if(len(visited)==len(guests)):
        pathlen()
    for g in guests:
        if guests[g]['visited']==0:
            guests[g]['visited']=1
            visited.append(g)
            recurse()
            visited.pop()
            guests[g]['visited']=0

with open('input.txt') as f:
    lines=f.readlines()

for line in lines:
    line=line.replace(".","")
    tokens=line.split()
    if tokens[0] not in guests:
        guests[tokens[0]]={'visited':0}
    if tokens[0] not in likehood:
        likehood[tokens[0]]={}
    if tokens[2]=="gain":
        likehood[tokens[0]][tokens[10]]=int(tokens[3])
    else:
        likehood[tokens[0]][tokens[10]]=-int(tokens[3])


recurse()
print("The overall Happyness is {}".format(happyness))
