with open('input.txt') as f:
    lines=f.readlines()

roll=0

for line in lines:
    x,y,z=line.strip().split("x")

    x=int(x)
    y=int(y)
    z=int(z)

    m=max(x,y,z)

    ribbon=(2*x+2*y+2*z-2*m)+(x*y*z)
    roll+=ribbon

print("Santa needs {} feet of ribbon".format(roll))
