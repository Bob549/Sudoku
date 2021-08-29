import numpy
import Solver
base  = 3
side  = base*base

# pattern for a baseline valid solution
def pattern(r,c): return (base*(r%base)+r//base+c)%side

# randomize rows, columns and numbers (of valid base pattern)
from random import sample
def shuffle(s): return sample(s,len(s)) 
rBase = range(base) 
rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
nums  = shuffle(range(1,base*base+1))

# produce board using randomized baseline pattern
board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]

#for line in board: print(line)
def createBoard(board):
    squares = side*side
    empties = squares * 3//4
    for p in sample(range(squares),empties):
        board[p//side][p%side] = 0

    numSize = len(str(side))
    return board
    #for line in board: print("["+"  ".join(f"{n or '0':{numSize}}" for n in line)+"]")



a = [[2, 5, 3, 7, 1, 4, 9, 8, 6],
 [7, 4, 8, 5, 6, 2, 1, 9, 3],
 [8, 2, 4, 1, 3, 5, 7, 6, 9],
 [1, 7, 5, 6, 8, 9, 2, 3, 4],
 [5, 8, 1, 9, 2, 3, 6, 4, 7],
 [3, 9, 2, 4, 5, 6, 8, 7, 1],
 [9, 6, 7, 3, 4, 8, 5, 1, 2],
 [6, 3, 9, 8, 7, 1, 4, 2, 5],
 [4, 1, 6, 2, 9, 7, 3, 5, 8]]

print(numpy.matrix(createBoard(a)))
Solver.solve(board)

