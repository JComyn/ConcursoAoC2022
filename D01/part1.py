with open("input.txt") as f:
    lines = f.readlines()

max_calories = 0
calories = 0
for line in lines:
    if line == '\n':
        if calories > max_calories:
            max_calories = calories
        calories = 0
    else:
        calories+=int(line)

print(max_calories)
