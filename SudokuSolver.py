# Solve a sudoku puzzle
import math
from Board import Board


class Solver:
    def __init__(self, board: Board):
        self.board = board

    def solve(self, resursions=0):
        '''
        Solve the puzzle
        '''

        # Examine each empty space in turn
        for i in range(self.board.size):
            for j in range(self.board.size):
                if (self.board.grid[i][j] != 0):
                    continue

                # Find possible values
                possible = self.poss_vals(i, j)

                # Make necessary changes
                if (len(possible) == 1):
                    self.board.grid[i][j] = possible[0]

    def poss_vals(self, i:int, j:int):
        '''
        Identify possible values that can be placed in a given slot

        args:
        i - row number
        j - column number
        '''

        poss = [x for x in range(1, self.board.size + 1)]

        for y in range(self.board.size):
            # Eliminate vals in same row
            if (self.board[i][y] in poss):
                poss.remove(self.board[i][y])

            # Eliminate vals in same column
            if (self.board[y][j] in poss):
                poss.remove(self.board[y][j])

        # Eliminate vals in same square
        rootSize = math.isqrt(self.board.size)

        for g in range(rootSize):
            for h in range(rootSize):
                cooX = (i // rootSize) + g
                cooY = (j // rootSize) + h

                if (self.board.grid[cooX][cooY] in poss):
                    poss.remove(self.board.grid[cooX][cooY])

        return poss

    