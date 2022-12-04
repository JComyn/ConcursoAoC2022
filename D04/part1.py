with open("input.txt") as f:
    pairs = [line.strip().split(",") for line in f.readlines()]

result = 0
for pair in pairs:
    first = pair[0].split("-")
    second = pair[1].split("-")
    f1 = int(first[0])
    f2 = int(first[1])
    s1 = int(second[0])
    s2 = int(second[1])
    if (f1 <= s1 and f2 >= s2) or (f1 >= s1 and f2 <= s2):
        result += 1

print(result)