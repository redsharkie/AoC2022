# First column meaning:
# A for Rock, B for Paper, and C for Scissors.

# Second columns meaning:
# X for Rock, Y for Paper, and Z for Scissors.
def get_shape(shape):
    if shape == 'A' or shape == 'X':
        return 'Rock'
    elif shape == 'B' or shape == 'Y':
        return 'Paper'
    elif shape == 'C' or shape == 'Z':
        return 'Scissors'
    else:
        return 'Input incorrect'


# The score for a single round is the score for the shape you selected
# (1 for Rock, 2 for Paper, and 3 for Scissors)
# plus the score for the outcome of the round
# (0 if you lost, 3 if the round was a draw, and 6 if you won).
def get_gameresult(a,b):
    a_shape = get_shape(a)
    b_shape = get_shape(b)
    if a_shape == 'Rock' and b_shape == 'Rock':
        return 3 + 1
    if a_shape == 'Paper' and b_shape == 'Paper':
        return 3 + 2
    if a_shape == 'Scissors' and b_shape == 'Scissors':
        return 3 + 3
    elif a_shape == 'Rock' and b_shape == 'Scissors':
        return 0 + 3
    elif a_shape == 'Rock' and b_shape == 'Paper':
        return 6 + 2
    elif a_shape == 'Scissors' and b_shape == 'Paper':
        return 0 + 2
    elif a_shape == 'Scissors' and b_shape == 'Rock':
        return 6 + 1
    elif a_shape == 'Paper' and b_shape == 'Rock':
        return 0 + 1
    elif a_shape == 'Paper' and b_shape == 'Scissors':
        return 6 + 3


score = 0
# Read file
with open ('input_day02.txt') as f:
    for line in f:
        gameinput = line.strip()
        a = gameinput[:1]
        b = gameinput[-1:]
        score += get_gameresult(a, b)
        print(score)
