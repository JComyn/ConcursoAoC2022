with open("input.txt") as f:
    rucksacks = f.readlines()

result = 0
for rucksack in rucksacks:
    half1 = rucksack[:len(rucksack)//2]
    half2 = rucksack[len(rucksack)//2:]
    common = ord(((set(half1)&(set(half2))).pop()))
    if common > 96: # lowercase
        result += common - 96
    else: # uppercase
        result += common - 38

print(result)