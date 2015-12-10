
def lookandsay(number):
    result = ""
 
    repeat = number[0]
    number = number[1:]+" "
    times = 1
 
    for actual in number:
        if actual != repeat:
            result += str(times)+repeat
            times = 1
            repeat = actual
        else:
            times += 1
 
    return result

input="1113222113"
for i in range(40):
    input = lookandsay(input)

print ("Part 1 = {}".format(len(input)))


input="1113222113"
for i in range(50):
    input = lookandsay(input)

print ("Part 2 = {}".format(len(input)))
