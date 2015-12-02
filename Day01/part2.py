file = open('input.txt', 'r')

floor=0
steps=0

while 1:
    char = file.read(1)          # read by character
    if not char: break
    steps+=1
    if char=="(": floor+=1
    if char==")": floor-=1
    if floor < 0: break


print("Santa returns to floor 0 after {} steps".format(steps))
file.close()
           
       
