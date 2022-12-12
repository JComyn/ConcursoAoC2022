stacks = [[],[],[],[],[],[],[],[],[]]
with open("input.txt") as f:
    lines = f.readlines()

# Read and store stacks
for line in lines:
    if line[1] == "1": break
    
    if line[1] != " ":
        stacks[0].append(line[1])
    if line[5] != " ":
        stacks[1].append(line[5])
    if line[9] != " ":
        stacks[2].append(line[9])
    if line[13] != " ":
        stacks[3].append(line[13])
    if line[17] != " ": 
        stacks[4].append(line[17])
    if line[21] != " ":
        stacks[5].append(line[21])
    if line[25] != " ":
        stacks[6].append(line[25])
    if line[29] != " ":
        stacks[7].append(line[29])
    if line[33] != " ":
        stacks[8].append(line[33])
    
# Movements
for i in range(9, len(lines)):
    temp = []
    if(len(lines[i]) < 20):
        move = (int)(lines[i][5])
        fr = (int)(lines[i][12])
        to = (int)(lines[i][17])
        for j in range(move):
            temp.append(stacks[fr-1].pop(0))
        stacks[to-1] = temp + stacks[to-1]
    elif (len(lines[i]) == 20):
        move = (int)(lines[i][5:7])
        fr = (int)(lines[i][13])
        to = (int)(lines[i][18])
        for j in range(move):
            temp.append(stacks[fr-1].pop(0))
        stacks[to-1] = temp + stacks[to-1]

# Print top of each stack
result = ""
for i in range(9):
    result += stacks[i][0]
print(result)
    
    