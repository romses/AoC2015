nice=0

with open('input.txt') as f:
    lines=f.readlines()



for line in lines:
    line=line.strip()
    pattern1=False
    pattern2=False
    for i in range(0,len(line)-1):
        pattern=line[i]+line[i+1]
        pos=line.find(pattern)
        pos2=line.find(pattern,pos+2)
        if pos2>0:
            pattern1=True
    for i in range(0,len(line)-2):
        pattern=line[i]+line[i+2] 
        if line[i]==line[i+2]:
            pattern2=True
    if pattern1==True and pattern2==True:
        nice+=1

print("Santas new list contains {} nice children".format(nice))

