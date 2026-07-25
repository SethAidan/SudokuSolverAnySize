import csv
import math


class Board:
    def __init__(self, grid=[], filename=""):
        '''
        Instantiate a grid object based on:
        A. A pre-populated 2d int list
        B. A CSV file
        '''

        # Ensure either a grid or filename is given
        if (filename == ""):
            if (grid == []):
                raise Exception("No grid or filename given")

        # Read CSV file into 2d list
        else:
            with open(filename, "r") as csvfile:
                reader = csv.reader(csvfile)
                grid = list(reader)

        # Ensure grid is valid
        if (not self.validate(grid)):
            raise Exception("Grid invalid")

        # Save attributes
        self.grid = grid
        self.size = len(grid)

    def validate(self, grid):
        '''
        Ensure grid follows rules
        1. grid is a 2d int list
        2. width and height equal
        3. width and height a square number
        4. every value between 0 and 9 (inclusive)
        '''

        # Ensure datastructure correct
        if (type(grid) != list[list[int]]):
            return False

        # Ensure size is square
        lines = len(grid)
        if (math.sqrt(lines) != math.floor(math.sqrt(lines))):
            return False

        for line in grid:
            # Ensure every line length matches num of lines
            if (len(line) != lines):
                return False

            # Ensure every value between 0 and 9
            for val in line:
                if (val < 0 or val > 9):
                    return False

        return True
