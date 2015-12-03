file = open('input.txt', 'r')

x=0
y=0

department={}
department[str(x)+"x"+str(y)]=1

#        ^ y
#        |
#        |
# <------+------>
#        |      x
#        |
#        v

while 1:
    char = file.read(1)          # read by character
    if not char: break
    if char=="^": y+=1
    if char=="v": y-=1
    if char==">": x+=1
    if char=="<": x-=1
    if(str(x)+"x"+str(y) not in department):
        department[str(x)+"x"+str(y)]=0
    department[str(x)+"x"+str(y)]+=1
    
print("{} of children gets at least one present!".format(len(department)))

file.close()
           
       
