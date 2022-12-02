PLAYER_PLAY = {
    "X": {
        "A": "Z",
        "B": "X",
        "C": "Y",
    },
    "Y": {
        "A": "X",
        "B": "Y",
        "C": "Z",
    },
    "Z": {
        "A": "Y",
        "B": "Z",
        "C": "X",
    },
}

SCORE_SHAPE = {
    "X": 1,
    "Y": 2, 
    "Z": 3
}

def main():
    with open("data.txt", 'r') as file:
        wins_player = 0
        for line in file:
            opponent_input, player_input = line.strip().split(" ")
            if player_input == "Z":
                wins_player += 6
            
            if player_input == "Y":
                wins_player += 3

            wins_player += SCORE_SHAPE[PLAYER_PLAY[player_input][opponent_input]]
        
        print(wins_player)

if __name__ == "__main__":
    main()