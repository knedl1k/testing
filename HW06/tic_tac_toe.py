# easy variant of the task No.6
# GNU General Public License v3.0
import sys
def load_matrix(filename):  # loads and stores matrix from file
    matrix = []
    f = open(filename, "r")
    for line in f:
        matrix.append(list(map(str, line.split())))
    f.close()
    return matrix
def count_char(char, matrix): #counts chars in matrix
    return sum([row.count(char) for row in matrix])
def check(enc_x, enc_y, col, row, act_pos, matrix): #makes sure it stays in the array
    if(enc_x>0 and col + abs(act_pos * enc_x) > (len(matrix[0]) - 1)):
        return False
    elif(enc_x < 0 and col - abs(act_pos * enc_x) < 0):
        return False
    if(enc_y>0 and row + abs(act_pos * enc_y) > len(matrix) - 1):
        return False
    elif(enc_y < 0 and row - abs(act_pos * enc_y) < 0):
        return False
    return True
def win_pos(matrix, char, enc_x, enc_y):
    seq_num = 0
    win_row, win_col = -1, -1
    win_amount = 5
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if (matrix[row][col] == char):
                seq_num += 1
                for i in range(1, win_amount+1):
                    if (not check(enc_x, enc_y, col, row, i, matrix)):
                        break
                    if (matrix[row + (i * enc_y)][col + (i * enc_x)] == char):
                        seq_num += 1
                    elif (matrix[row + (i * enc_y)][col + (i * enc_x)] == '.' and seq_num == win_amount - 1):
                        win_row = row + i * enc_y
                        win_col = col + i * enc_x
                        return win_row, win_col
                    else:
                        break
            seq_num = 0
    return -1, -1
def searching(matrix, char):
    for enc_x in range(-1, 2, 1):
        for enc_y in range(-1, 2, 1):
            if (enc_x == 0 and enc_y == 0):
                continue
            win_row, win_col = win_pos(matrix, char, enc_x, enc_y)
            if (win_row != -1):
                return win_row, win_col
    return -1,-1
if __name__ == "__main__":
    filename = sys.argv[1]  # při nahrání do BRUTE odkomentovat
    #filename = "6/tic_tac_toe.txt"
    matrix = load_matrix(filename)
    if(count_char('o',matrix)>count_char('x',matrix)):
        char='x'
    else:
        char='o'
    win_row, win_col=searching(matrix, char)
    print(win_row, win_col)
