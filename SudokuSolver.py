#Solve a sudoku puzzle
import math;

# Allow the user to input (with validation) the size of the sudoku grid (must be a square number)
def input_size():
    #Get size of puzzle
    valid = False
    while valid != True:
        try:
            size = int(input("Enter the number of columns in the sudoku puzzle : "))
            if(math.sqrt(size) % 1 == 0):
                valid = True
            else:
                print("Must be a square number")
        except:
            print("Must be a valid integer")
    return size

# Allow the user to input (with validation) their sudoku grid
def input_puzzle(size):
    #Get value for each square in puzzle
    print("Use 0 to indicate an empty space")
    puzz = []
    for i in range(0,size):
        valid = False
        while(valid != True):
            line = input(f"Enter line {i+1} : ")
            lineArr = line.split(' ')
            lineNumArr = []
            try:
                valid = True
                for num in lineArr:
                    if((int(num) > size) or (int(num) < 0)):
                        print(f"Please only use numbers in the range 0-{size}")
                        valid = False
                    else:
                        lineNumArr.append(int(num))
                if(len(lineNumArr) != size):
                    print(f"Please enter {size} values")
                    valid = False
            except:
                print("Please only enter numbers")
                valid = False
        puzz.append(lineNumArr)
    
    return puzz

# Return a list of all possible values a box could be
def check_box(grid, size, i, j):
    # Ensures rest of code only executed if the square is empty
    if(grid[i][j] != 0):
        return []
    
    poss = list(range(1,size+1)) #Initialised with every possible value and then wittled down
    col = list(row[j] for row in grid)
    root = math.sqrt(size)
    rem = list()

    # Iterate through each possible number, eliminating any it cannot be from the list
    for num in poss:
        if(num in grid[i]):
            rem.append(num) # Num cannot be removed from poss during iteration as this will affect the indexes and cause some values to be skipped
        elif(num in col):
            rem.append(num)
        else:
            # Possibly an easier/more efficient way to do this
            for k in range(int((i//root) * root),int(((i//root)*root)+root)):
                for l in range(int((j//root) * root),int(((j//root)*root)+root)):
                    if(grid[k][l] == num):
                        rem.append(num)
    for item in rem:
        poss.remove(item)
    return poss

# Checks whether a box can contain a specific number
def check_box_num(grid, size, i, j, num):
    # Ensures rest of code only executed if the square is empty
    if(grid[i][j] != 0):
        return False
    
    poss = True
    col = list(row[j] for row in grid)
    root = math.sqrt(size)

    # Iterate through each possible number, eliminating any it cannot be from the list
    if(num in grid[i]):
        poss = False
    elif(num in col):
        poss = False
    else:
        # Possibly an easier/more efficient way to do this
        # Checks the sub grid (usually 3x3 but not necessarily)
        for k in range(int((i//root) * root),int(((i//root)*root)+root)):
            for l in range(int((j//root) * root),int(((j//root)*root)+root)):
                if(grid[k][l] == num):
                    poss = False
    return poss

# Return a list of all the possible places in a row a number could appear
def check_row(grid, size, i, num):
    row = grid[i]
    poss = []
    if num in row:
        return []
    
    for j in range(0, size):
        if(check_box_num(grid, size, i, j, num)):
            poss.append([i,j])

    return poss

# Return a list of all the possible places in a column a number could appear
def check_col(grid, size, j, num):
    col = list(row[j] for row in grid)
    poss = []
    if num in col:
        return []
    
    for i in range(0, size):
        if(check_box_num(grid, size, i, j, num)):
            poss.append([i,j])

    return poss

# Return a list of all the possible places in a square a number could appear
def check_square(grid, size, i, j, num):
    root = int(math.sqrt(size))
    poss = []
    for k in range(int((i//root) * root),int(((i//root)*root)+root)):
                for l in range(int((j//root) * root),int(((j//root)*root)+root)):
                    if(check_box_num(grid, size, k, l, num)):
                        poss.append([k,l])

    return poss

# Checks if the sudoku has been fully solved
def solved(grid, size):
    for i in range(0, size):
        for j in range(0, size):
            if(grid[i][j] == 0):
                return False
    return True

# Solve the puzzle
def solver(grid, size):
    

    while(solved(grid, size) == False):
        change = True
        while(change):
            change = False
            for i in range(0,size):
                for j in range(0,size):
                    pos = check_box(grid, size, i,j)
                    if(len(pos) == 1 and grid[i][j] == 0):
                        grid[i][j] = pos[0]
                        change = True
        
        for num in range(0, size):
            for i in range(0, size):
                pos = check_row(grid, size, i ,num)
                if(len(pos) == 1):
                    grid[pos[0][0]][pos[0][1]] = num
                
                pows = check_col(grid, size, i, num)
                if(len(pos) == 1):
                    grid[pos[0][0]][pos[0][1]] = num

                for j in range(0, size):
                    pos = check_square(grid, size, i, j, num)
                    if(len(pos) == 1):
                        grid[pos[0][0]][pos[0][1]] = num


    return grid

# Call the relevant subroutines in order and output the result
def main():
    size = input_size()
    grid = input_puzzle(size)
    grid = solver(grid, size)

    for line in grid:
        print(line)

main()


        
