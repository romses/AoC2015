file = open('input.txt', 'r')

floor=0

while 1:
    char = file.read(1)          # read by character
    if not char: break
    if char=="(": floor+=1
    if char==")": floor-=1


print("Santa ends up in floor {}".format(floor))
file.close()
           
       
