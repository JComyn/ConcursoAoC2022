with open("input.txt") as f:
    rucksacks = f.readlines()

result = 0
i = 0
while i < len(rucksacks):
    elf1 = rucksacks[i][:-1] # remove newline
    elf2 = rucksacks[i+1][:-1]
    elf3 = rucksacks[i+2][:-1]
    i += 3
    common = ord(((set(elf1)&(set(elf2))&set(elf3)).pop())) # find common letter
    if common > 96: # lowercase
        result += common - 96
    else: # uppercase
        result += common - 38

print((result))