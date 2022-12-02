with open("input.txt") as f:
    rounds = f.readlines()

score = 0
for round in rounds:
    user = round[2]
    opponent = round[0]
    #Rock
    if user == 'X':
        score += 1
        if opponent == 'A': #Rock
            score += 3
        elif opponent == 'B': #Paper
            score += 0
        elif opponent == 'C': #Scissors
            score += 6

    #Paper
    elif user == 'Y':
        score += 2
        if opponent == 'A':
            score += 6
        elif opponent == 'B':
            score += 3
        elif opponent == 'C':
            score += 0

    #Scissors
    elif user == 'Z':
        score += 3
        if opponent == 'A':
            score += 0
        elif opponent == 'B':
            score += 6
        elif opponent== 'C':
            score += 3

print(score)