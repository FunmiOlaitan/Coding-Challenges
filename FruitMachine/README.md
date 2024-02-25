# 🍒🔔🍋🍊⭐💀 Fruit Machine

This project is a simple implementation of a fruit machine game written in Python. In this game, players can simulate playing a classic fruit machine and experience the thrill of winning or losing credits based on the symbols rolled.

## How to Play

1. Run the Python script `fruit_machine.py`.
2. You will start with an initial credit of £1.
3. The game will prompt you to decide whether you want to play the Fruit Machine.
4. If you choose to play, the machine will deduct £0.20 from your initial credit.
5. The machine will roll three symbols.
6. Depending on the outcome, you may win or lose credits.
7. The game will continue until you choose not to play or your credit drops below £0.20.

## Symbols

The fruit machine includes the following symbols:
- 🍒 Cherry
- 🔔 Bell
- 🍋 Lemon
- 🍊 Orange
- ⭐ Star
- 💀 Skull

## Winning and Losing Conditions

- **Three Skulls:** If you roll three skulls, you lose all your money.
- **Two Skulls:** If you roll two skulls, you lose £1.
- **Three Bells:** If you roll three bells, you win £5.
- **Three of the Same Symbol (except Skulls and Bells):** If you roll three of the same non-skull, non-bell symbols, you win £1.
- **Two of the Same Symbol:** If you roll two of the same symbols, you win £0.50.
- **No Win:** If you don't meet any of the above conditions, you don't win anything.

## Exiting the Game

You can exit the game at any time by choosing not to play when prompted. Your final credit will be displayed when you exit.

## Note

This is a basic implementation of a fruit machine game. Feel free to modify and expand upon it to add more features or improve the gameplay experience. Enjoy playing!