# minimax_tictactoe.py
import math

# Players
MAX = 'O'   # Maximizing Player
MIN = 'X'   # Minimizing Player

# Global board and counter
board = [' ' for _ in range(9)]
move_count = 0  # counts minimax recursive calls


def print_board(b):
    print()
    for i in range(3):
        print(" " + " | ".join(b[i*3:(i+1)*3]))
        if i < 2:
            print("-----------")
    print()


def check_winner(b):
    win_patterns = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for (x, y, z) in win_patterns:
        if b[x] == b[y] == b[z] and b[x] != ' ':
            return b[x]
    return None


def is_full(b):
    return ' ' not in b


def minimax(b, is_maximizing):
    """Return evaluation score for board b from perspective of MAX (O)."""
    global move_count
    move_count += 1

    winner = check_winner(b)
    if winner == MAX:
        return 1
    if winner == MIN:
        return -1
    if is_full(b):
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = MAX
                score = minimax(b, False)
                b[i] = ' '
                if score > best:
                    best = score
        return best
    else:
        best = math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = MIN
                score = minimax(b, True)
                b[i] = ' '
                if score < best:
                    best = score
        return best


def best_move_for(player):
    """
    Returns the index (0-8) of the best move for `player` (MAX or MIN).
    Defensive: if no moves available returns None.
    """
    available = [i for i in range(9) if board[i] == ' ']
    if not available:
        return None

    if player == MAX:
        best_score = -math.inf
        best_move = None
        for i in available:
            board[i] = MAX
            score = minimax(board, False)  # after MAX move, MIN plays
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
        return best_move
    else:
        best_score = math.inf
        best_move = None
        for i in available:
            board[i] = MIN
            score = minimax(board, True)   # after MIN move, MAX plays
            board[i] = ' '
            if score < best_score:
                best_score = score
                best_move = i
        return best_move


def play_auto(starting_player=MAX, show_steps=True):
    """Automatically play a full game with both sides using Minimax."""
    global board, move_count
    board = [' ' for _ in range(9)]
    move_count = 0

    current = starting_player
    if show_steps:
        print("Starting automatic Tic-Tac-Toe (Minimax).")
        print_board(board)

    while True:
        move = best_move_for(current)
        if move is None:
            # board full or no move possible
            break
        board[move] = current
        if show_steps:
            print(f"{current} plays at position {move + 1}")
            print_board(board)

        winner = check_winner(board)
        if winner:
            if show_steps:
                print(f"🏆 Winner: {winner}")
            break
        if is_full(board):
            if show_steps:
                print("It's a Draw!")
            break

        current = MIN if current == MAX else MAX

    if not check_winner(board) and is_full(board):
        print("Final: Draw")
    elif check_winner(board):
        print(f"Final Winner: {check_winner(board)}")
    else:
        print("Final: Game ended unexpectedly (no moves)")

    print(f"Total minimax recursive calls (explored positions): {move_count}")


if __name__ == "__main__":
    # Run with O (MAX) starting. Change to MIN to let X start.
    play_auto(starting_player=MAX, show_steps=True)
