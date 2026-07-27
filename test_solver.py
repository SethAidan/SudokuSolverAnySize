import pytest
from Board import Board
from SudokuSolver import Solver

def read_grid(filename):
    grid = []
    with open(filename, "r") as file:
        for line in file:
            grid.append([int(num) for num in line.split(" ")])

    return grid

# Overall tests
@pytest.mark.parametrize("puzzle_name", [
    "nine-A",
    "nine-B",
    "nine-C",
    "nine-D",
    "nine-E",
    "nine-F",
    "nine-G",
])

def test_9(puzzle_name):
    grid = read_grid(f"test/Puzzles/{puzzle_name}")
    ans = read_grid(f"test/Solutions/{puzzle_name}")

    bd = Board(grid)
    sv = Solver(bd)
    sv.solve()

    assert bd.grid == ans