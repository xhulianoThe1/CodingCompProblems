### Part 1 ####
f = open('input_2.txt', 'r').readlines()
hor, depth, aim = 0, 0, 0 
for i in f: 
    inp = i.split(" ")
    if inp[0] == 'forward': 
        hor += int(inp[1]) 
    elif inp[0] == 'up': 
        depth -= int(inp[1]) 
    else: 
        depth += int(inp[1])  
print(hor*depth)

### Part 2 ####
f = open('input_2.txt', 'r').readlines()
hor, depth, aim = 0, 0, 0 
for i in f: 
    inp = i.split(" ")
    if inp[0] == 'forward': 
        hor += int(inp[1]) 
        depth += int(inp[1])*aim
    elif inp[0] == 'up': 
        aim -= int(inp[1]) 
    else: 
        aim += int(inp[1]) 
print(hor*depth)
