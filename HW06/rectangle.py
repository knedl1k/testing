#!/usr/bin/env python3
# difficult variant of the task No.6
# GNU General Public License v3.0
import os
import sys
import time
def load_matrix(filename): # stores matrix from file into 2D array
    matrix=[]
    with open(filename,"r") as f:
        for line in f:
            matrix.append(list(map(int,line.split())))
    return matrix
def reset(matrix):
    return len(matrix),-1
def max_rectangle(matrix):
    col=len(matrix[0])
    left=[0]*col #left and right boundary and height of the rectangle
    right=[col]*col
    height=[0]*col
    max_area=0 # maximum area and the corner coordinates of the rectangle
    top_left=(0,0)
    bot_right=(0,0)
    for row in range(len(matrix)): #iterate over each row of the matrix
        cur_left,cur_right=0,col
        for i in range(col):# if the current cell is negative, increment the height of the rectangle at that column
            if (matrix[row][i]<0):
                height[i] += 1
            else: #if the current cell is not negative, reset the height of the rectangle at that column
                height[i]=0
        for j in range(col):#left
            if (matrix[row][j]<0):
                left[j]=max(left[j],cur_left)
            else:
                left[j],cur_left=0,j + 1
        for k in range(col-1,-1,-1): #right
            if (matrix[row][k]<0):
                right[k]=min(right[k],cur_right)
            else:
                right[k],cur_right=col,k
        for l in range(col):#stores values for the biggest matrix
            if ((right[l]-left[l])*height[l]>max_area):
                max_area=(right[l]-left[l])*height[l]
                top_left=(row-height[l]+1,left[l])
                bot_right=(row,right[l]-1)
    return max_area,top_left,bot_right
if __name__=="__main__":
    #startTime=time.time()
    filename=sys.argv[1] if len(sys.argv)>1 else "/home/knedl1k/Desktop/B3B33ALP/assignments/6/rectangle.txt" 
    max_area,top_left,bottom_right=max_rectangle(load_matrix(filename))
    #print(max_area)
    print(top_left[0],top_left[1])
    print(bottom_right[0],bottom_right[1])
    #executionTime=(time.time()-startTime)
    #print("cas: ",executionTime)
