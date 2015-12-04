import md5
import re

puzzle="bgvyzdsv"
number=0
hex=""
i=0

while('00000'!=hex):
    i+=1
    clear=puzzle+str(i)
    m=md5.new()
    m.update(clear)
    hex=m.hexdigest()[:5]

print("The first coin is {}".format(i))
