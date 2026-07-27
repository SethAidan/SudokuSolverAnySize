# Sudoku Solver

A simple Python program that solves Sudoku puzzles with varying grid sizes—so long as the height and width are both the same square number. The solver uses logical deduction to determine an appropriate solution to the puzzle.

## Features
- User-friendly input validation for grid size and puzzle entries.
- Supports variable-sized Sudoku puzzles (4x4, 9x9, 16x16, etc.).
- Implements linear recursion with backtracking to efficiently solve the puzzle

## How It Works
1. The user enters the size of the Sudoku puzzle.
2. The user inputs the puzzle row by row, using `0` to indicate empty spaces.
3. The program determines possible values for each cell based on Sudoku rules using a combination of the following:
   - Finds the only place a number could fit in a specific row/column/square.
   - If that fails it picks one possible solution.
4. The solver recurses, backtracking if no solution can be found.
5. The completed Sudoku grid is displayed.

## Installation & Usage

### Prerequisites
Check you have a valid version of Python 3 installed on your computer using:
```console
python --version
```
or
```console
python3 --version
```

If not install it from [here](https://www.python.org/downloads/)
### Running the Program
1. Clone this repository
```console
git clone https://github.com/SethAidan/SudokuSolverAnySize.git sudoku-solver
cd sudoku-solver
```
2. Run the script
```console
python Main.py
```
or
```console
python3 Main.py
```

### Example Input/Output

Input:
```console
Enter the number of columns in the sudoku puzzle : 9

Now enter the puzzle itself
Use 0 to indicate an empty space
Enter line 1 : 0 0 0 0 9 1 0 7 8
Enter line 2 : 0 7 0 4 0 0 0 0 0
Enter line 3 : 0 9 6 0 0 2 0 5 0
Enter line 4 : 0 0 7 8 1 0 0 9 5
Enter line 5 : 0 0 9 0 5 4 0 8 0
Enter line 6 : 6 0 0 0 0 0 0 0 0
Enter line 7 : 2 0 0 0 0 0 0 0 4
Enter line 8 : 0 0 0 0 0 9 0 1 0
Enter line 9 : 0 5 0 0 0 0 0 0 0
...
```
Output:
```console
5 4 2 3 9 1 6 7 8
8 7 3 4 6 5 1 2 9
1 9 6 7 8 2 4 5 3
4 2 7 8 1 6 3 9 5
3 1 9 2 5 4 7 8 6
6 8 5 9 3 7 2 4 1
2 6 1 5 7 8 9 3 4
7 3 8 6 4 9 5 1 2
9 5 4 1 2 3 8 6 7
...
```
