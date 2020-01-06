# battleship-game
The aim is to create a battleship game where computer's move is as smart as humans and where computer can beat a human.

This game is in single player mode:
1.Place your own ships.
2.The computer places its ships immediately.
3.As soon as you have shot, the computer shoots and you are immediately back on turn.

Each player starts with a fleet of 5 ships, of length 5, 4, 3, 3, and 2.
Each player places their ships horizontally or vertically on a 10x10 grid; this is not visible to their opponent.
Players take turns to fire at positions on the grid, gradually revealing where their opponent’s ships are and are not located.
A ship is destroyed when every cell of a ship has been hit.
The winner is the first player to destroy their opponent’s fleet.

You lose if:

1.You do not place the correct number and size of ships.
2.You place your fleet in impossible positions (ships overlapping or partly off the board).
3.Your code raises an exception.
4.All your ships have been sunk.
