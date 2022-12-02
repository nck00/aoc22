my_total_score_A = 0
my_total_score_B = 0

def calc_score_part_A(other: str, mine: str) -> int:
    # other:    A: Rock
    #           B: Paper
    #           C: Scissors
    # mine:     X: Rock     -> +1
    #           Y: Paper    -> +2
    #           Z: Scissors -> +3
    # Outcomes: Lose:       -> +0
    #           Draw:       -> +3
    #           Win:        -> +6
    total_score = 0
    my_play_scores = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }
    total_score += my_play_scores[mine]
    if other == "A":
        if mine == "X":
            total_score += 3
        elif mine == "Y":
            total_score += 6
        elif mine == "Z":
            total_score += 0
    elif other == "B":
        if mine == "X":
            total_score += 0
        elif mine == "Y":
            total_score += 3
        elif mine == "Z":
            total_score += 6
    elif other == "C":
        if mine == "X":
            total_score += 6
        elif mine == "Y":
            total_score += 0
        elif mine == "Z":
            total_score += 3
    return total_score

def calc_score_part_B(other: str, outcome: str) -> int:
    # other:    A: Rock
    #           B: Paper
    #           C: Scissors
    # mine:     Rock        -> +1
    #           Paper       -> +2
    #           Scissors    -> +3
    # Outcomes: X: Lose:    -> +0
    #           Y: Draw:    -> +3
    #           z: Win:     -> +6
    total_score = 0
    outcome_scores = {
        "X": 0,
        "Y": 3,
        "Z": 6
    }
    total_score += outcome_scores[outcome]
    if other == "A":
        if outcome == "X":
            mine = "S"
        elif outcome == "Y":
            mine = "R"
        elif outcome == "Z":
            mine = "P"
    elif other == "B":
        if outcome == "X":
            mine = "R"
        elif outcome == "Y":
            mine = "P"
        elif outcome == "Z":
            mine = "S"
    elif other == "C":
        if outcome == "X":
            mine = "P"
        elif outcome == "Y":
            mine = "S"
        elif outcome == "Z":
            mine = "R"
    my_play_scores = {
        "R": 1,
        "P": 2,
        "S": 3
    }
    total_score += my_play_scores[mine]
    return total_score

with open("input.txt") as f:
    for line in f:
        other, mine = line.strip("\n").split(" ")
        my_total_score_A += calc_score_part_A(other, mine)
        my_total_score_B += calc_score_part_B(other, mine)
print("Part A:", my_total_score_A)
print("Part B:", my_total_score_B)

    
