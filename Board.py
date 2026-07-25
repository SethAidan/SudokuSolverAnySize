import math


class Board:
    def __init__(self, grid=None, filename=""):
        '''
        Instantiate a grid object based on:
        A. A pre-populated 2d int list
        B. A CSV file
        '''

        # Ensure either a grid or filename is given
        if (filename == "" and grid is None):
            raise ValueError("No grid or filename given")

        # Read file into 2d list
        else:
            grid = []
            with open(filename, "r") as file:
                for line in file:
                    grid.append([int(num) for num in line.split(" ")])

        # Ensure grid is valid
        valid, reason = self.validate(grid)
        if (not valid):
            raise ValueError(f"Grid invalid: {reason}")

        # Save attributes
        self.grid = grid
        self.size = len(grid)

    @staticmethod
    def validate(grid):
        '''
        Ensure grid follows rules
        1. grid is a 2d int list
        2. width and height equal
        3. width and height a square number
        4. every value between 0 and size (inclusive)
        '''

        # Ensure at least list
        if (not isinstance(grid, list)):
            return False, f"Top level not a list, {type(grid)}"

        # Ensure size is square
        lines = len(grid)
        root = math.isqrt(lines)
        if (root * root != lines):
            return False, "Num lines not square"

        for line in grid:
            # Ensure 2d list
            if (not isinstance(line, list)):
                return False, "Not a 2d list"
                        
            # Ensure every line length matches num of lines
            if (len(line) != lines):
                return False, f"line does not match num of lines: {line}"

            # Ensure every value between 0 and size
            for val in line:
                if ((not isinstance(val, int)) or val < 0 or val > lines):
                    return False, f"Invalid value: {val}"

        return True, "All good"

    def display_grid(self):
        '''
        Print grid as a 2d grid
        '''
        for line in self.grid:
            print(" ".join(str(val) for val in line))
