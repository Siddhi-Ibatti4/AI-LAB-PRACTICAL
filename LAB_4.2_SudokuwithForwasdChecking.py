def find_unassigned(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None, None

def is_valid(board, row, col, num):
    # Row and column check
    if num in board[row] or num in [board[r][col] for r in range(9)]:
        return False
    # 3x3 subgrid check
    start_row, start_col = 3*(row//3), 3*(col//3)
    for r in range(start_row, start_row+3):
        for c in range(start_col, start_col+3):
            if board[r][c] == num:
                return False
    return True

def forward_checking(board, row, col):
    domain = {i: set(range(1, 10)) for i in range(81)}
    for r in range(9):
        for c in range(9):
            if board[r][c] != 0:
                idx = r*9 + c
                domain[idx] = {board[r][c]}
    return domain

def solve_sudoku(board):
    row, col = find_unassigned(board)
    if row is None:
        return True

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False

# Example puzzle
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
solve_sudoku(sudoku_board)
for row in sudoku_board:
    print(row)

