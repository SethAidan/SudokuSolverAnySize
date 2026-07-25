from Board import Board
from SudokuSolver import Solver
import math

def input_size():
    '''
    Return the user defined size of the Sudoku grid
    Must be a square number
    '''
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
    return size


def input_puzzle(size):
    '''
    Take and return puzzle input
    Empty squares are stored as a 0 (which can not occur in a valid puzzle)
    '''
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


def read_csv():
    '''
    Import sudoku from csv for debugging
    '''
    grid = []

    with open("test.csv", "r") as file:
        for line in file:
            ln = line.strip().split(" ")
            lni = [int(n) for n in ln]
            grid.append(lni)

    return grid


def main():
    '''
    Call the relevant subroutines in order and output the result
    '''
    bd = Board(filename="test.csv")
    solver = Solver(bd)
    solver.solve()


main()