#!/usr/bin/env python3
# difficult variant of the task No.07
# GNU General Public License v3.0
import sys
def load_matrix(filename): #loads input
    with open(filename,"r") as file:
        num_col,num_row=list(map(int,file.readline().strip().split())) # first 2 nums
        matrix=[]
        for row in range(num_row):  #loads gaming board
            matrix_row=list(map(int,file.readline().strip().split()))
            matrix.append(matrix_row)
        pieces=[]
        for line in file:
            piece=[]
            whole=list(map(int,line.strip().split()))
            for i in range(len(whole)//2):
                row,col=whole[2*i+0],whole[2*i+1]
                row-=whole[0]
                col-=whole[1]
                piece.append([row,col])
            pieces.append(piece)
    #print(matrix)
    return matrix,pieces
def pretty_print(matrix): #prints the output board
    for row in range (len(matrix)):
        for col in range(len(matrix[row])):
            if (col<len(matrix[row])-1):
                print(matrix[row][col],end=" ")
            else:
                print(matrix[row][col]) #the last number in the row
def is_inside(row,col,matrix): #checks boundaries
    return (row>=0 and row<len(matrix) and col>=0 and col<len(matrix[row]))
def can_place(piece,row,col,matrix): #checks if it is possible to place new piece
    for cell in piece:
        row_c,col_c=cell
        new_row=row_c+row
        new_col=col_c+col
        if not (is_inside(new_row,new_col,matrix) and matrix[new_row][new_col]==0):
            return False
    return True
def get_rotation(piece,rot_enc): #using encoding returns rotation of a piece
    if (rot_enc==0):
        return piece
    elif (rot_enc==1):
        return [[-col,row] for row,col in piece]
    elif (rot_enc==2):
        return [[-row,-col] for row,col in piece]
    else:
        return [[col,-row] for row,col in piece]
def get_solution(matrix,piece_num,pieces): #does all the magic
    if (piece_num==len(pieces)): 
        if not (0 in matrix): #if there is no space left, game is over, prints the board
            #print(matrix)
            pretty_print(matrix)
            sys.exit()
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            for rot_enc in range(4): #rotation encoding
                piece=get_rotation(pieces[piece_num],rot_enc) #returns rotated piece
                if (can_place(piece,row,col,matrix)):
                    for cell in piece: #place the piece on the board
                        row_c,col_c=cell
                        matrix[row_c+row][col_c+col]=piece_num+1
                    get_solution(matrix,piece_num+1,pieces) #recursive call 
                    for cell in piece: #remove the piece from the board because it was invalid move
                        row_c,col_c=cell
                        matrix[row_c+row][col_c+col]=0
if __name__=="__main__":
    filename=sys.argv[1] if len(sys.argv)>1 else "/home/knedl1k/Desktop/B3B33ALP/assignments/7/ubongo.txt" 
    matrix,pieces=load_matrix(filename)
    get_solution(matrix,0,pieces)
