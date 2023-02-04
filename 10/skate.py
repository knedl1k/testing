#!/usr/bin/env python3
# easy variant of the task No.10
# GNU General Public License v3.0
import sys
import collections
def find_path(matrix, direction, row, col, history):
    if (direction=="Z"):
        while (col-1>=0 and matrix[row][col-1]!=1):
            col-=1
    elif (direction=="S"):
        while (row-1>=0 and matrix[row-1][col]!=1):
            row-=1
    elif (direction=="J"):
        while (row+1<len(matrix) and matrix[row+1][col]!=1):
            row+=1
    else:
        while (col+1<len(matrix[0]) and matrix[row][col+1]!=1):
            col+=1
    return row,col,history+direction
if __name__ == "__main__":
    #filename="skate1.txt"
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        lines=f.readlines()
    matrix=[]
    for line in lines:
        matrix.append([int(x) for x in line.strip().split()])
    start,end=None,None
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 2:
                start=(row, col)
            elif matrix[row][col] == 4:
                end=(row, col)
    attempts=collections.deque([(start[0], start[1], "")])
    visited=set()
    while attempts:
        attempt=attempts.popleft()
        if attempt[:2] in visited:
            continue
        visited.add(attempt[:2])
        for direction in "ZSVJ":
            new_attempt=find_path(matrix, direction, attempt[0], attempt[1], attempt[2])
            if new_attempt[:2] == end:
                print(new_attempt[2])
                quit()
            else:
                attempts.append(new_attempt)
