with open("input.txt") as f:
    rounds = f.readlines()

score = 0
for round in rounds:
    opponent = round[0]
    result = round[2] # X lose, Y draw, Z win
    #Rock
    if opponent == 'A':
        if result == 'X': 
            score += 3 + 0
        elif result == 'Y': 
            score += 1 + 3
        elif result == 'Z': 
            score += 2 + 6
    #Paper
    elif opponent == 'B':
        if result == 'X':
            score += 1 + 0
        elif result == 'Y':
            score += 2 + 3
        elif result == 'Z':
            score += 3 + 6
    #Scissors
    elif opponent == 'C':
        if result == 'X':
            score += 2 + 0
        elif result == 'Y':
            score += 3 + 3
        elif result== 'Z':
            score += 1 + 6

print(score)