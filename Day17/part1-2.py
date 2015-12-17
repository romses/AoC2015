with open('input.txt') as f:
    lines=f.readlines()

bottles=[]

for line in lines:
    bottles.append(int(line))

solutions=0
minimalAmount=len(bottles)

for i in range(2**len(bottles)):
    capacity=0
    tmpamount=0
    for pos in range(len(bottles)):
        if i&(2**pos):
            capacity+=bottles[pos]
            tmpamount+=1
    if capacity==150:
        solutions+=1
        if tmpamount<minimalAmount:
            minimalAmount=tmpamount

print("Santa has {} possibilities to store his eggnog".format(solutions))
print("Santa needs at least {} bottles".format(minimalAmount))
