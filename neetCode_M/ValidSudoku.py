# You are given a a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:
# Each row must contain the digits 1-9 without duplicates.
# Each column must contain the digits 1-9 without duplicates.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
# Return true if the Sudoku board is valid, otherwise return false
# Note: A board does not need to be full or be solvable to be valid.

COL_SUDOKU = 9
ROW_SUDOKU = 9
SIGN = '.'

def sudoku(board) :
    rows = [set() for _ in range(ROW_SUDOKU)]
    cols = [set() for _ in range(COL_SUDOKU)]
    cube = [[set() for _ in range(3)] for _ in range(3)]  # 3x3 grid

    for i in range(ROW_SUDOKU):
        for j in range(COL_SUDOKU):
            val = board[i][j]
            if val != SIGN:
                if (val in rows[i]) or (val in cols[j]) or (val in cube[i // 3][j // 3]):
                    return False
                else:
                    rows[i].add(val)
                    cols[j].add(val)
                    cube[i // 3][j // 3].add(val)
    return True



board = [
    ["5","3",".",".","9",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

print(sudoku(board))