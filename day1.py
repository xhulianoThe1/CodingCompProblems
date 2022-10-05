### Read in input ### 
f = open('input_1.txt', 'r').readlines()
inp = [int(x) for x in f] 

### Part 1 ###
count = 0 
curr = inp[0]

for idx, val in enumerate(inp): 
    if val > curr: 
        count += 1 
    curr = val
print(count)
  
### Part 2 ### 
count = 0 
prev =  sum(inp[:3])
for idx, val in enumerate(inp): 
    curr = sum(inp[idx:idx+3])
    if curr > prev: 
        count +=1 
    prev = sum(inp[idx:idx+3]) 
print(count)    
