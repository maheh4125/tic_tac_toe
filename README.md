# Tic-Tac-Toe AI with Minimax Algorithm

This project implements a Tic-Tac-Toe game where a human player can play against an AI opponent that uses the Minimax algorithm to make optimal moves.

## How to Play

1. **Run the Python script:** `python tic_tac_toe.py` (replace `tic_tac_toe.py` with the actual filename if you saved it differently).
2. **Enter your moves:** The game board is displayed with numbered rows and columns (1-3).  When prompted, enter your move in the format `row,col`, using 1-based indexing.  For example, to place your mark in the top-right corner, enter `1,3`.
3. **The AI plays:** The AI will automatically make its move after you.
4. **Game continues:** The game continues until one player wins or the board is full (a draw).

## AI Algorithm

The AI opponent uses the Minimax algorithm. Minimax is a recursive algorithm used for decision-making in game theory and artificial intelligence. It explores all possible game states up to a certain depth and assigns a score to each state, representing how favorable that state is for the AI.  The AI chooses the move that leads to the state with the highest score (assuming the opponent plays optimally).

## Code Overview

The code is structured as follows:

* **`print_board(board)`:** Prints the Tic-Tac-Toe board in a user-friendly format with 1-indexed rows and columns.
* **`evaluate(board)`:** Evaluates the current board state and returns 1 if 'X' (AI) wins, -1 if 'O' (human) wins, and 0 otherwise (draw or game in progress).
* **`is_moves_left(board)`:** Checks if there are any empty spaces left on the board.
* **`minimax(board, depth, is_maximizing)`:** The core Minimax algorithm implementation.  Recursively explores the game tree and returns the best possible score for the current player.
* **`find_best_move(board)`:** Uses the Minimax algorithm to determine the AI's best move.
* **`play_game()`:**  Manages the game loop, taking player input, making AI moves, and checking for win/draw conditions.

## Requirements

* Python 3

## How to Run

1. Make sure you have Python 3 installed.
2. Save the code as a `.py` file (e.g., `tic_tac_toe.py`).
3. Open a terminal or command prompt.
4. Navigate to the directory where you saved the file.
5. Run the command `python tic_tac_toe.py`.


## Potential Enhancements

* **GUI:** Add a graphical user interface for a more visually appealing game.
* **Difficulty Levels:** Implement different difficulty levels by adjusting the depth of the Minimax search.
* **Other Algorithms:** Explore alternative game-playing algorithms like Monte Carlo Tree Search.
