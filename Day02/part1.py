with open('input.txt') as f:
    lines=f.readlines()

roll=0

for line in lines:
    x,y,z=line.strip().split("x")

    x=int(x)
    y=int(y)
    z=int(z)

    m=max(x,y,z)

    paper=(2*x+2*y+2*z)+(x*y*z/m)
    roll+=paper

print("Santa needs {} square feet of paper".format(roll))
