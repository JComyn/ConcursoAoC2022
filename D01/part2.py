with open("input.txt") as f:
    lines = f.readlines()

calories = 0
total=[]
for line in lines:
    if line == '\n':
        total.append(calories)
        calories = 0
    else:
        calories+=int(line)

total.sort(reverse=True)
print(total[0]+total[1]+total[2])
