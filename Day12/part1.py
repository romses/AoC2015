balance=0

with open('input.txt') as f:
    lines=f.readlines()

lines[0]=lines[0].replace("{"," ")
lines[0]=lines[0].replace("}"," ")
lines[0]=lines[0].replace(":"," ")
lines[0]=lines[0].replace(","," ")
lines[0]=lines[0].replace("["," ")
lines[0]=lines[0].replace("]"," ")


tokens=lines[0].split()

for token in tokens:
    try:
        balance+=int(token)
    except:
        pass

print("Santas Banc balance is {}".format(balance))
