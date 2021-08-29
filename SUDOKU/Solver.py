import numpy
import random as rd


grid = [[5,3,0,0,7,0,0,0,0,],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]

base = [[1,2,3,  4,5,6,  7,8,9],
        [4,5,6,  7,8,9,  1,2,3],
        [7,8,9,  1,2,3,  4,5,6],
        [2,3,1,  5,6,4,  8,9,7],
        [5,6,4,  8,9,7,  2,3,1],
        [8,9,7,  2,3,1,  5,6,4],
        [3,1,2,  6,4,5,  9,7,8],
        [6,4,5,  9,7,8,  3,1,2],
        [9,7,8,  3,1,2,  6,4,5]]

#x column, y row, n number
def possible(x, y, n, grid):
#check
    #rows
    for j in range(0,9):
        if grid[x][j] == n:
            return False
    #column
    for i in range(0,9):
        if grid[i][y] == n:
            return False
    #3x3
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[x0 + i][y0 + j] == n:
                return False
    #else
    return True

base = 3
side = 9

def expandLine(line):
    return line[0]+line[5:9].join([line[1:5]*(base-1)]*base)+line[9:13]



def design(grid):
    line0  = expandLine("╔═══╤═══╦═══╗")
    line1  = expandLine("║ . │ . ║ . ║")
    line2  = expandLine("╟───┼───╫───╢")
    line3  = expandLine("╠═══╪═══╬═══╣")
    line4  = expandLine("╚═══╧═══╩═══╝")

    symbol = " 1234567890ABCDEFGHIJKLMNOPQRSTVWXYZ"
    nums   = [ [""]+[symbol[n] for n in row] for row in grid ]
    print(line0)
    for r in range(1,side+1):
        print( "".join(n+s for n,s in zip(nums[r-1],line1.split("."))) )
        print([line2,line3,line4][(r%side==0)+(r%base==0)])

a = 0
def solve(grid):
    
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for n in range(1, 10):
                    if possible(i, j, n, grid):
                        grid[i][j] = n                     
                        solve(grid)
                        grid[i][j] = 0
                return
    design(grid)
    return
    input("More?")






