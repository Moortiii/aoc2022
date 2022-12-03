with open("input.txt", "r") as f:
    data = f.readlines()
    data = [line.strip() for line in data]

POINTS_PER_CHOICE = {
    "X": 1, # Rock
    "Y": 2, # Paper
    "Z": 3, # Scissors
}

POINTS_PER_TIE = 3
POINTS_PER_LOSS = 0
POINTS_PER_WIN = 6

mapping = {
    "AX": POINTS_PER_CHOICE["X"] + POINTS_PER_TIE,
    "AY": POINTS_PER_CHOICE["Y"] + POINTS_PER_WIN,
    "AZ": POINTS_PER_CHOICE["Z"] + POINTS_PER_LOSS,

    "BX": POINTS_PER_CHOICE["X"] + POINTS_PER_LOSS,
    "BY": POINTS_PER_CHOICE["Y"] + POINTS_PER_TIE,
    "BZ": POINTS_PER_CHOICE["Z"] + POINTS_PER_WIN,
    
    "CX": POINTS_PER_CHOICE["X"] + POINTS_PER_WIN,
    "CY": POINTS_PER_CHOICE["Y"] + POINTS_PER_LOSS,
    "CZ": POINTS_PER_CHOICE["Z"] + POINTS_PER_TIE,
}

total_points = 0

for line in data:
    game = "".join(line.replace(" ", ""))
    total_points += mapping[game]

print("Total points:", total_points)