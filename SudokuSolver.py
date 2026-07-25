# Solve a sudoku puzzle
import math
from Board import Board


class Solver:
    def __init__(self, board: Board):
        self.board = board

    def check_box(self, i, j):
        '''
        Return a list of all possible values a box could be
        '''
        # Ensures rest of code only executed if the square is empty
        if (self.board.grid[i][j] != 0):
            return []

        # Poss initialised with every possible value and then wittled down
        poss = list(range(1, self.board.size+1))
        col = list(row[j] for row in self.board.grid)
        root = math.sqrt(self.board.size)
        rem = list()

        # Iterate over possible numbers, removing impossible ones from list
        for num in poss:
            if (num in self.board.grid[i]):
                # Num cannot be removed from poss during iteration
                # This would affect the indexes and cause values to be skipped
                rem.append(num)
            elif (num in col):
                rem.append(num)
            else:
                # Possibly an easier/more efficient way to do this
                minK = int((i//root) * root)
                maxK = int(((i//root)*root)+root)
                for indexK in range(minK, maxK):
                    minL = int((j//root) * root)
                    maxL = int(((j//root)*root)+root)
                    for indexL in range(minL, maxL):
                        if (self.board.grid[indexK][indexL] == num):
                            rem.append(num)
        for item in rem:
            poss.remove(item)
        return poss

    def check_box_num(self, i, j, num):
        ''' Return (bool) whether a box can contain a specific number
        '''
        # Ensures rest of code only executed if the square is empty
        if (self.board.grid[i][j] != 0):
            return False

        poss = True
        col = list(row[j] for row in self.board.grid)
        root = math.sqrt(self.board.size)

        # Iterate through each possible number
        # Eliminate any it cannot be from the list
        if (num in self.board.grid[i]):
            poss = False
        elif (num in col):
            poss = False
        else:
            # Possibly an easier/more efficient way to do this
            # Checks the sub grid (usually 3x3 but not necessarily)
            minK = int((i//root) * root)
            maxK = int(((i//root)*root)+root)
            for indexK in range(minK, maxK):
                minL = int((j//root) * root)
                maxL = int(((j//root)*root)+root)
                for indexL in range(minL, maxL):
                    if (self.board.grid[indexK][indexL] == num):
                        poss = False
        return poss

    def check_row(self, i, num):
        '''
        Return a list of all the possible places in a row a number could appear
        '''
        row = self.board.grid[i]
        poss = []
        if num in row:
            return []

        for j in range(0, self.board.size):
            if (self.check_box_num(i, j, num)):
                poss.append([i, j])

        return poss

    def check_col(self, i, j, num):
        '''
        Return a list of all the possible places in a col a number could appear
        '''
        col = list(row[j] for row in self.board.grid)
        poss = []
        if num in col:
            return []

        for i in range(0, self.board.size):
            if (self.check_box_num(i, j, num)):
                poss.append([i, j])

        return poss

    def check_square(self, i, j, num):
        '''
        Return a list of all possible places in a square a number could appear
        '''
        root = int(math.sqrt(self.board.size))
        poss = []
        for indexK in range(int((i//root) * root), int(((i//root)*root)+root)):
            for indexL in range(int((j//root) * root),
                                int(((j//root)*root)+root)
                                ):
                if (self.check_box_num(indexK, indexL, num)):
                    poss.append([indexK, indexL])

        return poss

    def solved(self):
        '''
        Checks if the sudoku has been fully solved
        '''

        for i in range(0, self.board.size):
            for j in range(0, self.board.size):
                if (self.board.grid[i][j] == 0):
                    return False
        return True

    def solve(self):
        '''
        Return the solved puzzle
        '''

        while (self.solved() is False):
            change = True
            while (change):
                change = False
                for i in range(0, self.board.size):
                    for j in range(0, self.board.size):
                        pos = self.check_box(i, j)
                        if (len(pos) == 1 and self.board.grid[i][j] == 0):
                            self.board.grid[i][j] = pos[0]
                            change = True

            for num in range(0, self.board.size):
                for i in range(0, self.board.size):
                    pos = self.check_row(i, num)
                    if (len(pos) == 1):
                        self.board.grid[pos[0][0]][pos[0][1]] = num

                    if (len(pos) == 1):
                        self.board.grid[pos[0][0]][pos[0][1]] = num

                    for j in range(0, self.board.size):
                        pos = self.check_square(i, j, num)
                        if (len(pos) == 1):
                            self.board.grid[pos[0][0]][pos[0][1]] = num

    def getGrid(self):
        return self.board.grid
