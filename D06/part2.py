with open("input.txt") as f:
    input = f.read()

found = False
i = 0
while not found:
    substring = input[i:i+14]
    # Convert i to set, so duplicates are removed
    if len(set(substring)) == len(substring):
        found = True
    else:
        i += 1

print(i+14)