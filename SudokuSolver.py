# Solve a sudoku puzzle
import math
from Board import Board


class Solver:
    def __init__(self, board: Board):
        self.board = board

    def solve(self):
        '''
        Solve the puzzle and ensure only valid solution saved
        '''
        ans, valid = self.next_state(self.board.grid, self.board.size)

        if (valid):
            self.board.grid = ans

        else:
            self.board.grid = ["Unsolveable"]

    def next_state(self, grid, size):
        '''
        Recursively solve sudoku puzzle
        '''

        next_i = -1
        next_j = -1
        queue = []
        changed = False

        for i in range(size):
            for j in range(size):
                # Ignore already filled cells
                if (grid[i][j] != 0):
                    continue

                # Find possible solutions
                possible = self.poss_vals(grid, i, j)

                # Apply the only possible solution
                if (len(possible) == 1):
                    grid[i][j] = possible[0]
                    changed = True

                # Store list of possible solutions for cell
                elif (len(possible) > 1):
                    next_i = i
                    next_j = j
                    queue = possible

        # Allow correct answer to propogate
        if (Board.solved(grid, size)):
            return grid, True

        # Only possible answer recurses forward
        elif (changed):
            return self.next_state(grid, size)

        # Cycle through possible solutions until correct found
        else:
            for val in queue:
                new_grid = [row[:] for row in grid]
                new_grid[next_i][next_j] = val
                new_grid, valid = self.next_state(new_grid, size)

                if (valid):
                    return new_grid, True

            return [], False

    def poss_vals(self, grid, i: int, j: int):
        '''
        Identify possible values that can be placed in a given slot

        args:
        i - row number
        j - column number
        '''

        poss = [x for x in range(1, self.board.size + 1)]

        for y in range(self.board.size):
            # Eliminate vals in same row
            if (grid[i][y] in poss):
                poss.remove(grid[i][y])

            # Eliminate vals in same column
            if (grid[y][j] in poss):
                poss.remove(grid[y][j])

        # Eliminate vals in same square
        rootSize = math.isqrt(self.board.size)

        # Eliminate vals in the same sub-square
        for g in range(rootSize):
            for h in range(rootSize):
                cooX = (i // rootSize) * rootSize + g
                cooY = (j // rootSize) * rootSize + h

                if (grid[cooX][cooY] in poss):
                    poss.remove(grid[cooX][cooY])

        return poss
