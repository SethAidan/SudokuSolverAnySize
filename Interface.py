from Board import Board
from SudokuSolver import Solver
import math

'''
def read_grid(filename):
    grid = []
    with open(filename, "r") as file:
        for line in file:
            grid.append([int(num) for num in line.split(" ")])

    return grid

grid = read_grid("test/Puzzles/nine-B")
ans = read_grid("test/Solutions/nine-B")

bd = Board(grid)
bd.display_grid()
sv = Solver(bd)
sv.solve()
print()
bd.display_grid()
'''

class Interface:
    def __init__(self):
        print("~~~~~~~~~~ Welcome ~~~~~~~~~~")

        # Either allow manual or file based entry
        method = self.input_q("How would you like to enter the puzzle?",["Manual input", "File"])
        if (method == 1):
            grid = self.type_puzzle()
            bd = Board(grid=grid)
            sv = Solver(bd)
            sv.solve()
            bd.display_grid()
        if (method == 2):
            filename = self.file_puzzle()
            bd = Board(filename=filename)
            sv = Solver(bd)
            sv.solve()
            bd.display_grid()

    def input_q(self, question:str, options:list):
        '''
        Ask a question with n possible answers
        Allow the user to answer by giving a number between 1 and n
        '''
        valid = False

        while (not valid):
            print(question)
            for i in range(len(options)):
                print(f"{i+1}. {options[i]}")

            answer = input("Choice : ")

            if (answer.isnumeric()):
                answer = int(answer)

                if (answer > 0 and answer <= len(options)):
                    return answer

                else:
                    print(f"Please enter a number between 1 and {len(options)}")

            else:
                print("Please enter a number")

            print()

    def type_puzzle(self):
        '''
        Allow user to manually type out their puzzle
        '''

        # Determine the size of the puzzle
        size = -1
        valid = False
        while valid is not True:
            try:
                size = int(
                    input("Enter the number of columns in the sudoku puzzle : "))
                if (math.sqrt(size) % 1 == 0):
                    valid = True
                else:
                    print("Must be a square number")
            except (ValueError):
                print("Must be a valid integer")

        # Accept the puzzle itself
        print()
        print("Now enter the puzzle itself")
        print("Use 0 to indicate an empty space")
        puzz = []
        for i in range(0, size):
            valid = False
            while (valid is not True):
                line = input(f"Enter line {i+1} : ")
                lineArr = line.split(' ')
                lineNumArr = []
                try:
                    valid = True
                    for num in lineArr:
                        if ((int(num) > size) or (int(num) < 0)):
                            print(f"Please only use numbers in the range 0-{size}")
                            valid = False
                        else:
                            lineNumArr.append(int(num))
                    if (len(lineNumArr) != size):
                        print(f"Please enter {size} values")
                        valid = False
                except (ValueError):
                    print("Please only enter numbers")
                    valid = False
            puzz.append(lineNumArr)

        return puzz

    def file_puzzle(self):
        '''
        Allow user to enter a filepath for a puzzle
        '''

        # Enter filename
        filename = input("Enter the name of the file : ")

        return filename

inter = Interface()