import random 

# Define the symbols
symbols = ["Cherry", "Bell", "Lemon", "Orange", "Star", "Skull"]

initial_player_credit = 1

def game_loop():
    global initial_player_credit
    while  initial_player_credit >= 0.2:
        print(f"Current Credit: £{initial_player_credit:.2f}")
        play_decision = input("Do you want to play Fruit Machine? (yes/no): ").lower

    if play_decision != "yes":
        print(f"Thanks for playing! Final Credit: £{initial_player_credit:.2f}")

    initial_player_credit -= 0.2
    
    # Implement symbol rolling
    rolled_symbols = []
    for _ in range(3):
        symbol = random.choice(symbols)  # selects a random element from the symbols list
        rolled_symbols.append(symbol)
        return rolled_symbols

    # Implement win/lose conditions
    outcome = "Rolled symbols: " + ','.join(rolled_symbols)
    if rolled_symbols.count("skull") == 3:
        outcome += "Three skulls! You lose all your money."
        initial_player_credit = 0
    elif rolled_symbols.count("skull") == 2:
        outcome += "Two skulls! You lose £1."
        initial_player_credit -= 1
    elif len(set(rolled_symbols)) == 1:
        if "Bell" in rolled_symbols:
            outcome += "Three Bells! You win £5."
            initial_player_credit += 5
        else:
            outcome += f"Three {rolled_symbols[0]}s! You win £1."
            initial_player_credit += 1
    elif len(set(rolled_symbols)) == 2:
        outcome += "Two of same symbols! You win 0.50p."
        initial_player_credit += 0.5
    else:
        outcome += "No win this time."
    
    print(outcome)

if __name__ == "__main__":
    game_loop()
