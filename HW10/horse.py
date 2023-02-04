#!/usr/bin/env python3
# difficult variant of the task No.10
# GNU General Public License v3.0
import sys
import collections
def find_path(matrix, direction, row, col, history): #bohuzel tu neni switch :(
    if (direction==1):
        if(row-2>-1 and col-1>-1 and matrix[row-2][col-1]!=1): #(-2, -1)
            row-=2
            col-=1
    elif (direction==2):
        if(row-2>-1 and col+1<len(matrix[0]) and matrix[row-2][col+1]!=1): #(-2, 1)
            row-=2
            col+=1
    elif (direction==3):
        if(row-1>-1 and col-2>-1 and matrix[row-1][col-2]!=1): #(-1, -2)
            row-=1
            col-=2
    elif (direction==4):
        if(row-1>-1 and col+2<len(matrix[0]) and matrix[row-1][col+2]!=1): #(-1, 2)
            row-=1
            col+=2
    elif (direction==5):
        if(row+1<len(matrix) and col-2>-1 and matrix[row+1][col-2]!=1): #(1, -2)
            row+=1
            col-=2
    elif (direction==6):
        if(row+1<len(matrix) and col+2<len(matrix[0]) and matrix[row+1][col+2]!=1): #(1, 2)
            row+=1
            col+=2
    elif (direction==7):
        if(row+2<len(matrix) and col-1>-1 and matrix[row+2][col-1]!=1): #(2, -1)
            row+=2
            col-=1
    else:
        if(row+2<len(matrix) and col+1<len(matrix[0]) and matrix[row+2][col+1]!=1): #(2, 1)
            row+=2
            col+=1
    return row,col,history+' '+str(row)+' '+str(col)
if __name__ == "__main__":
    filename="horse1.txt"
    #filename = sys.argv[1]
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
    tahy=[1,2,3,4,5,6,7,8]
    while attempts:
        attempt=attempts.popleft()
        if attempt[:2] in visited:
            continue
        visited.add(attempt[:2])
        for direction in tahy:
            new_attempt=find_path(matrix, direction, attempt[0], attempt[1], attempt[2])
            if new_attempt[:2] == end:
                #print(new_attempt[2][0])
                print(new_attempt[2][1:])
                quit()
            else:
                attempts.append(new_attempt)
    print("NEEXISTUJE") #if fails to find any path, the path is non-existent
