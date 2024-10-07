#!/usr/bin/python3
import sys


def print_solution(board):
    """
    Print the current board solution as a list
    of [row, col] positions.
    """

    solution = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 1:
                solution.append([row, col])
    print(solution)


def is_safe(board, row, col, N):
    """Check if a queen can be placed at board[row][col]."""
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col, N):
    """Use backtracking to solve the N queens problem."""
    if col >= N:
        print_solution(board)
        return True

    res = False
    for row in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1  # Place the queen

            res = solve_nqueens(board, col + 1, N) or res

            board[row][col] = 0  # Backtrack

    return res


def nqueens(N):
    """Initialize the board and start the N queens solution process."""
    board = [[0 for _ in range(N)] for _ in range(N)]
    solve_nqueens(board, 0, N)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(N)
