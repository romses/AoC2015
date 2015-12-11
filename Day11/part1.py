input="hepxcrrq"

def increase(password,position=-1):
    if position==-1: position=len(password)-1

    left=password[0:position]
    mid=password[position]
    right=password[position+1:]

    mid=ord(mid)+1
    if mid ==105 or mid == 108 or mid == 111:
        mid+=1
    if mid > 122:
        mid=mid-26
        return increase(left+chr(mid)+right,position-1)
    mid=chr(mid)
    return left+mid+right

def pwd_ok(pwd):
    strait_ok=False
    letters_ok=True
    pairs_ok=0

    for i in range(len(pwd)-2):
        a=ord(pwd[i+2])
        b=ord(pwd[i+1])
        c=ord(pwd[i])
        if (a==b+1) and (b==c+1):
            strait_ok=True

    if "i" in pwd:letters_ok=False
    if "o" in pwd:letters_ok=False
    if "l" in pwd:letters_ok=False

    for i in range(97,123):
        pattern=chr(i)+chr(i)
        if(pattern in pwd):
            pairs_ok+=1

    return(strait_ok and letters_ok and (pairs_ok>=2))



input=increase(input)

while not pwd_ok(input):
    input=increase(input)
print("Santas first new Password is  {}".format(input))

input=increase(input)
while not pwd_ok(input):
    input=increase(input)

print("Santas second new Password is {}".format(input))
