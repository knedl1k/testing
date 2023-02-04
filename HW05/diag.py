# easy variant of the task No.5
# GNU General Public License v3.0
import sys
def load_matrix(filename): #loads and stores input matrix
    matrix = []
    f = open(filename, "r")
    for line in f:
        matrix.append(list(map(int, line.split())))
    f.close()
    return matrix
def storing(sum_elem, pos_row, pos_col, f_ele, f_row, f_col): #stores all values if the sum of elements is greater
    if (sum_elem > f_ele):
        f_ele = sum_elem
        f_row = pos_row
        f_col = pos_col
    sum_elem = 0
    return sum_elem, f_ele, f_row, f_col
def searching(matrix, diag): #searches for the biggest diagonal of even numbers
    sum_ele, f_ele = 0, 0
    f_row, f_col = -1, -1
    pos_row, pos_col = -1, -1
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if (matrix[row][col] % 2 == 0):  # firt even num in the diagonal
                col_active = col #stores its coordinates
                row_active = row
                sum_ele += 1 # it's the first number, so 0+1
                pos_row = row
                pos_col = col
                while (0 <= col_active + diag <= len(matrix[row])-1 and row_active < len(matrix)-1): # do this until you reach limits
                    if (matrix[row_active + 1][col_active + diag ] % 2 == 0): # is the next num in diagonal even?
                        sum_ele += 1
                        col_active += diag
                        row_active += 1
                    else: # if the next num in the diagonal is not even, stop while
                        break
                sum_ele, f_ele, f_row, f_col = storing(sum_ele, pos_row, pos_col, f_ele, f_row, f_col)
            else:
                sum_ele, f_ele, f_row, f_col = storing(sum_ele, pos_row, pos_col, f_ele, f_row, f_col)
    return f_row, f_col, f_ele
if __name__ == "__main__":
    filename = sys.argv[1]  # při nahrání do BRUTE odkomentovat
    #filename = "diag.txt"
    matrix = load_matrix(filename)
    ff_row, ff_col, ff_ele = searching(matrix, 1) #ff-firstFinal, left to right diagonal
    sf_row, sf_col, sf_ele = searching(matrix, -1) #sf-secondFinal, right to left diagonal
    if (ff_ele > sf_ele):
        print(ff_row, ff_col, ff_ele)
    else:
        print(sf_row, sf_col, sf_ele)
