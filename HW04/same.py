# easy variant of the task No.4
# GNU General Public License v3.0
def finding(input_nums, pos, num): #searches for the same numbers in the array
    for i in range(pos, len(input_nums)):
        if(num == input_nums[i]):
            return i
def storing(final_l, pos_f, pos_s, length, final_f, final_s): #saves values to output
    if(length > final_l):
        final_l = length
        final_f = pos_f
        final_s = pos_s
    return final_l, final_f, final_s
def searching(input_nums):
    length, pos_f, pos_c = -1, -1, -1
    final_l, final_f, final_s = -1, -1, -1
    new_seq = 1
    for pos_f in range(len(input_nums) - 1):
        length = 0
        for i in range(len(input_nums) - 1):
            if(input_nums[pos_f] in input_nums[pos_f + 1:]): #determine the leading element = must be at least 2x in the array
                if (new_seq == 1):#stores the position of the second identical sequence if it is a new sequence
                    pos_c = finding(input_nums, pos_f + 1, input_nums[pos_f]) #hleda kamarada k vedoucimu prvku
                while(input_nums[pos_f + length] == input_nums[pos_c + length]): #will run until the end of array if the nums are same
                    length += 1
                    if(pos_f + length == pos_c) or (pos_c + length == len(input_nums)): #stops if its the end of array
                        break
                final_l, final_f, final_s = storing(final_l, pos_f, pos_c, length, final_f, final_s)
                length = 0
                if(input_nums[pos_f] not in input_nums[pos_c + 1:]): #sequence has broken, restarts temp variables
                    pos_f, pos_c = 0, 0
                    new_seq = 1
                    break
                else:
                    pos_c = finding(input_nums, pos_c + 1, input_nums[pos_f])
                    new_seq = 0
            else:
                break
    return final_l, final_f, final_s
if __name__ == "__main__":
    input_nums = (list(map(int, input().split())))
    final_l,final_f,final_s=searching(input_nums)
    print(final_l,final_f,final_s)
