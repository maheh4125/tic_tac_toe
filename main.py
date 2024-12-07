import math

def print_board(board):
    print("  1 2 3")
    for i, row in enumerate(board):
        print(i + 1, "|".join(row))
        if i < 2:
            print("  -----")

def evaluate(board):
    for row in board:
        if all(x == row[0] and x != ' ' for x in row):
            return 1 if row[0] == 'X' else -1 if row[0] == 'O' else 0
    for col in range(3):
        if all(board[row][col] == board[0][col] and board[0][col] != ' ' for row in range(3)):
            return 1 if board[0][col] == 'X' else -1 if board[0][col] == 'O' else 0
    if all(board[i][i] == board[0][0] and board[0][0] != ' ' for i in range(3)):
        return 1 if board[0][0] == 'X' else -1 if board[0][0] == 'O' else 0
    if all(board[i][2 - i] == board[0][2] and board[0][2] != ' ' for i in range(3)):
        return 1 if board[0][2] == 'X' else -1 if board[0][2] == 'O' else 0
    return 0

def is_moves_left(board):
    return any(' ' in row for row in board)

def minimax(board, depth, is_maximizing):
    score = evaluate(board)
    if score == 1: return score - depth
    if score == -1: return score + depth
    if not is_moves_left(board): return 0

    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = ' '
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = ' '
        return best

def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_val = minimax(board, 0, False)
                board[i][j] = ' '
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    while True:
        print_board(board)
        while True:
            try:
                row, col = map(int, input("Enter your move (row, col, 1-indexed): ").split(","))
                row -= 1  # Adjust to 0-index
                col -= 1  # Adjust to 0-index
                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                    board[row][col] = 'O'
                    break
                else:
                    print("Invalid move. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Enter two numbers (1-3) separated by a comma.")


        if evaluate(board) == -1: print_board(board); print("You win!"); break
        if not is_moves_left(board): print_board(board); print("It's a draw!"); break

        ai_move = find_best_move(board)
        board[ai_move[0]][ai_move[1]] = 'X'

        if evaluate(board) == 1: print_board(board); print("AI wins!"); break
        if not is_moves_left(board): print_board(board); print("It's a draw!"); break

if __name__ == "__main__":
    play_game()
