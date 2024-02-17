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
