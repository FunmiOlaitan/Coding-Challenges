import random 

# Define the symbols
symbols = ["Cherry", "Bell", "Lemon", "Orange", "Star", "Skull"]

initial_player_credit = 1.0

def game_loop():
    global initial_player_credit
    while initial_player_credit > 0.2:  # strictly greater than 0.2
        print(f"Current Credit: £{initial_player_credit:.2f}")
        play_decision = input("Do you want to play Fruit Machine? (yes/no): ").lower()
        
        if play_decision != "yes":
            print(f"Thanks for playing! Final Credit: £{initial_player_credit:.2f}")
            break

        initial_player_credit -= 0.2
        initial_player_credit = round(initial_player_credit, 2)
        
        # Implement symbol rolling
        rolled_symbols = [random.choice(symbols) for _ in range(3)]

        # Implement win/lose conditions
        outcome = "Rolled symbols: " + ','.join(rolled_symbols)
        if rolled_symbols.count("Skull") == 3:
            outcome += ". Three skulls! You lose all your money."
            initial_player_credit = 0
        elif rolled_symbols.count("Skull") == 2:
            outcome += ". Two skulls! You lose £1."
            initial_player_credit -= 1
        elif len(set(rolled_symbols)) == 1:
            if "Bell" in rolled_symbols:
                outcome += ". Three Bells! You win £5."
                initial_player_credit += 5
            else:
                outcome += f". Three {rolled_symbols[0]}s! You win £1."
                initial_player_credit += 1
        elif len(set(rolled_symbols)) == 2:
            outcome += ". Two of the same symbols! You win 50p."
            initial_player_credit += 0.5
        else:
            outcome += ". No win this time."
        
        initial_player_credit = round(initial_player_credit, 2)
        print(outcome)
        if initial_player_credit < 0.2:
            print("You've run out of credit.")
            break

if __name__ == "__main__":
    game_loop() 