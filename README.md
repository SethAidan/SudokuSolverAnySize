# Sudoku Solver

A simple Python program that solves Sudoku puzzles with varying grid sizes—so long as the height and width are both the same square number. The solver uses logical deduction to determine an appropriate solution to the puzzle.

## Features
- User-friendly input validation for grid size and puzzle entries.
- Supports variable-sized Sudoku puzzles (4x4, 9x9, 16x16, etc.).
- Implements logical techniques to solve the puzzle without brute-force backtracking.

## How It Works
1. The user enters the size of the Sudoku puzzle.
2. The user inputs the puzzle row by row, using `0` to indicate empty spaces.
3. The program determines possible values for each cell based on Sudoku rules using a combination of the following:
   - Finds the only place a number could fit in a specific row/column/square.
   - Finds the only number a specific cell can contain.
4. The solver iterates through logical elimination techniques until the puzzle is solved.
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
python sudoku_solver.py
```
or
```console
python3 sudoku_solver.py
```

### Example Input/Output

Input:
```console
Enter the number of columns in the sudoku puzzle: 9
Use 0 to indicate an empty space
Enter line 1: 5 3 0 0 7 0 0 0 0
Enter line 2: 6 0 0 1 9 5 0 0 0
...
```
Output:
```console
[5, 3, 4, 6, 7, 8, 9, 1, 2]
[6, 7, 2, 1, 9, 5, 3, 4, 8]
...
```
## Code Breakdown

 - `input_size()`: Ensures the user enters a valid Sudoku grid size.

 - `input_puzzle(size)`: Takes a valid Sudoku grid input from the user.

 - `check_box(grid, size, i, j)`: Determines possible values for an empty cell.

 - `check_row(grid, size, i, num)`: Finds possible placements of a number in a row.

 - `check_col(grid, size, j, num)`: Finds possible placements of a number in a column.

 - `check_square(grid, size, i, j, num)`: Finds possible placements of a number in a subgrid.

 - `solved(grid, size)`: Checks if the puzzle is completely solved.

 - `solver(grid, size)`: Iteratively solves the puzzle using logical techniques.

 - `main()`: Runs the entire program.

## License

This project is open-source and available under the [MIT License](https://mit-license.org/).
