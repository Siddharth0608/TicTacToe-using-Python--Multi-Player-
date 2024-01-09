# Tic-Tac-Toe Game Implementation in Python (Multiplayer)
This GitHub repository contains a simple implementation of the classic Tic-Tac-Toe game using Python. The code includes classes for players (human and computer), the game board, and a main script for playing the game.

## Key Features:

### Player Classes:

Player: A base class representing a generic player with a method get_move to be implemented by subclasses.
HumanPlayer: A subclass of Player, representing a human player who can input moves via the console.
RandomComputerPlayer: A subclass of Player, representing a computer player making random moves.

### Tic-Tac-Toe Class:

Represents the game board and its state.
Methods include print_board, print_board_nums, available_moves, make_move, empty_squares, empty_squares_num, and winner.

### Game Play Function:

The play function takes instances of the Tic-Tac-Toe class and two players, allowing them to play the game. It handles moves, prints the board, and declares the winner or a tie.

### Main Script:

The script initializes a HumanPlayer ('X') and a RandomComputerPlayer ('O') to play against each other.
Creates an instance of the Tic-Tac-Toe class and calls the play function to start the game.
