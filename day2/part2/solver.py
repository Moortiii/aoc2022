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

outcome_mapping = {
    "A": {
        "tie": "X",
        "win": "Y",
        "loss": "Z" 
    },
    "B": {
        "tie": "Y",
        "win": "Z",
        "loss": "X"
    },
    "C": {
        "tie": "Z",
        "win": "X",
        "loss": "Y"
    }
}

choice_mapping = {
    "X": "loss",
    "Y": "tie",
    "Z": "win"
}

total_points = 0

for line in data:
    game = "".join(line.replace(" ", ""))

    opponent_choice, player_choice = game
    expected_outcome = choice_mapping[player_choice]
    
    # Determine what to play
    move_to_play = outcome_mapping[opponent_choice][expected_outcome]

    # Calculate the score if we play to the expected outcome
    actual_game = opponent_choice + move_to_play

    total_points += mapping[actual_game]

print("Total points:", total_points)