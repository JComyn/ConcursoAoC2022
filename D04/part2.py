with open("input.txt") as f:
    pairs = [line.strip().split(",") for line in f.readlines()]

result = len(pairs)
for pair in pairs:
    first = pair[0].split("-")
    second = pair[1].split("-")
    f1 = int(first[0])
    f2 = int(first[1])
    s1 = int(second[0])
    s2 = int(second[1])
    if (f2 < s1) or (s2 < f1):
        result -= 1

print(result)