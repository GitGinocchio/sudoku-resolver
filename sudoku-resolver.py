MAX = 9

SUDOKU = [
    [1,0,0,0,0,0,0,5,9],
    [0,7,8,5,0,0,0,1,6],
    [0,9,3,0,8,0,4,0,0],
    [0,1,0,0,6,5,0,0,0],
    [0,0,7,8,0,9,1,0,0],
    [0,0,0,1,3,0,0,8,0],
    [0,0,1,0,7,0,5,3,0],
    [7,8,0,0,0,3,6,4,0],
    [4,3,0,0,0,0,0,0,8]
]

def solve_sudoku(sudoku):
    if is_complete(sudoku):
        return sudoku

    row, col = find_empty_cell(sudoku)
    for num in range(1, MAX+1):
        if is_valid(sudoku, row, col, num):
            sudoku[row][col] = num
            if solve_sudoku(sudoku):
                return sudoku
            else:
                sudoku[row][col] = 0

    return None

def is_complete(sudoku):
    for row in sudoku:
        if 0 in row:
            return False
    return True

def find_empty_cell(sudoku):
    for row in range(MAX):
        for col in range(MAX):
            if sudoku[row][col] == 0:
                return row, col
    return None

def is_valid(sudoku, row, col, num):
    for i in range(MAX):
        if sudoku[row][i] == num or sudoku[i][col] == num:
            return False

    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if sudoku[box_row + i][box_col + j] == num:
                return False

    return True

solution = solve_sudoku(SUDOKU)
if solution is not None:
    print("Sudoku solved:")
    for row in solution:
        print(row)
else:
    print("No solution found.")