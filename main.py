'''
Libraries:
-py-sudoku
-pygame

-Use backtraking algorithm to solve a sudoku
-First do text version of sudoku and the algorithm to solve it
-Then make the game in pygame and integrate the backtraking algorithm to solve it
'''

class Sudoku():
    def __init__(self):
        self.board = [[0, 2, 6, 0, 0, 0, 0, 0, 3],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [7, 0, 0, 0, 4, 8, 0, 6, 0],
                      [0, 7, 0, 0, 0, 1, 0, 0, 0],
                      [0, 4, 0, 2, 0, 5, 0, 0, 9],
                      [2, 0, 0, 0, 8, 0, 0, 5, 7],
                      [5, 0, 8, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 2, 0],
                      [0, 0, 0, 0, 1, 0, 5, 4, 0]]
    
    def is_valid_number(self, row, col, digit):
        '''
        Checks if it's valid to put a number in a certain square
        '''

        # Checks row
        if digit in self.board[row]:
            return False
        
        # Checks col
        for i in range(9):
            if digit == self.board[i][col]:
                return False
        

        # Checks 3x3 box
        box_start_row = (row // 3) * 3
        box_start_col = (col // 3) * 3
        for i in range(box_start_row, box_start_row + 3):
            for j in range(box_start_col, box_start_col + 3):
                if digit == self.board[i][j]:
                    return False
        
        return True
    

    def find_empty_cell(self):
        '''
        Finds the cells that need to be completed
        '''

        for r in range(9):
            for c in range(9):
                if self.board[r][c] == 0:
                    return r, c
        return None, None
        
    def solve(self):
        '''
        Solves the board using backtracking algorithm
        '''

        # Finds the first empty cell
        row, col = self.find_empty_cell()

        # If there is not any empty cell the board is solved
        if row is None:
            return True

        # Searches for a value for the empty cell
        for val in range(1, 10):
            if self.is_valid_number(row, col, val):
                self.board[row][col] = val

                # Using recursion to solve the rest of the board
                if self.solve():
                    return True
            
            # Reseting the cell
            self.board[row][col] = 0

        # Backtracking to the previous cell if no value is valid
        return False

    def print_solution(self):
        for row in self.board:
            print(row)



sudoku = Sudoku()

sudoku.solve()
sudoku.print_solution()


