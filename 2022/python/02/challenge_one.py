PLAYER_WINS = {
    "X": "C", 
    "Y": "A", 
    "Z": "B"
}

PLAYER_DRAW = {
    "X": "A", 
    "Y": "B", 
    "Z": "C"
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
            if PLAYER_WINS[player_input] == opponent_input:
                wins_player += 6
            
            if PLAYER_DRAW[player_input] == opponent_input:
                wins_player += 3

            wins_player += SCORE_SHAPE[player_input]
        
        print(f"You wins wtih {wins_player} points")

if __name__ == "__main__":
    main()