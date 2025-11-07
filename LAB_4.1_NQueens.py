def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i] == col:
            return False
        if abs(board[i] - col) == abs(i - row):  # diagonal attack
            return False
    return True

def forward_check(board, row, col, n, domains):
    new_domains = [d.copy() for d in domains]
    for r in range(row+1, n):
        if col in new_domains[r]:
            new_domains[r].remove(col)
        diag1 = col + (r - row)
        diag2 = col - (r - row)
        if diag1 in new_domains[r]:
            new_domains[r].remove(diag1)
        if diag2 in new_domains[r]:
            new_domains[r].remove(diag2)
    return new_domains

def solve_nqueens(board, row, n, domains):
    if row == n:
        return [board[:]]
    solutions = []
    for col in domains[row]:
        if is_safe(board, row, col, n):
            board[row] = col
            new_domains = forward_check(board, row, col, n, domains)
            if all(new_domains[r] for r in range(row+1, n)):
                solutions += solve_nqueens(board, row+1, n, new_domains)
    return solutions

n = 8
domains = [list(range(n)) for _ in range(n)]
solutions = solve_nqueens([-1]*n, 0, n, domains)
print("Number of solutions:", len(solutions))
print("One solution:", solutions[0])

