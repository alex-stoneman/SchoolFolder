import numpy as np

def display_queens(board):
    for line in board:
        for cell in line:
            if cell == 1:
                print("X", end=" ")
            else:
                print("o", end =" ")
        print()
    print()

def queens_lines(board, pos, change, n):
    # pos = [row, column]
    board[pos[0]][pos[1]] += change
    for y in range(n):
        if y != pos[0]:
            board[y][pos[1]] += 2 * change
    for x in range(n):
        if x != pos[1]:
            board[pos[0]][x] += 2 * change
    for a in [-1, 1]:
        for b in [-1, 1]:
            current = pos.copy()
            while True:
                current = [current[0] + a, current[1] + b]
                if 0 <= current[0] < n and 0 <= current[1] < n:
                    board[current[0]][current[1]] += 2 * change
                else:
                    break
    return board


def row_check(n, row, board, solutions):
    for y in range(n):
        if board[row][y] == 0:
            if row == n - 1:
                board = queens_lines(board, [row, y], 1, n)
                display_queens(board)
                solutions += 1
                board = queens_lines(board, [row, y], -1, n)
            else:
                board = queens_lines(board, [row, y], 1, n)
                solutions = row_check(n, row + 1, board, solutions)
                board = queens_lines(board, [row, y], -1, n)
    return solutions



def queens_not_killing(n):
    # 0 = unused, 1 = queen, 2+ = can't go
    solutions = 0
    board = np.zeros((n, n), dtype=int)
    print(row_check(n, 0, board, 0))



queens_not_killing(int(input()))