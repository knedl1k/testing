#difficult variant of the task No.2
#GNU General Public License v3.0
def error():  # if called, prints 'ERROR' and terminates program
    print("ERROR")
    quit()
    return None
def entry_control(sys_base,in_num):  # checks correctness of input and also returns the position of the dot in the number
    dots_num = 0
    dot_pos = -1
    num1=0
    for i in range(len(in_num)):
        if ('a' <= in_num[i] <= 'z'):  # translates letters into num values
            num1 = ord(in_num[i]) - 87
        elif (in_num[i] == '.'):  # looks for a dot in a number
            dot_pos = i
            dots_num += 1
        else:
            num1 = ord(in_num[i]) - 48
        if (num1 >= sys_base or num1 < 0 or dot_pos == 0 or dots_num > 1):  # searches for the wrong number of dots and nums same or higher than sys_base
            error()
    return dot_pos
def conv_mantissa(num, dot_pos):  # returns value of a mantissa
    if (dot_pos == -1):  # if the number is integer, no mantissa is needed
        return num, -1
    else:  # otherwise it is necessary to shift the number by enough to make it integer
        moved_num = []
        mantissa = len(num) - dot_pos - 1
        for i in range(len(num)):
            if (num[i] != '.'):
                moved_num.append(num[i])
            else:
                continue
        return moved_num, mantissa  # returns value of moved_num and also mantissa for it
def multiply(sys_base, first, second):  # multiply both numbers with each other and returns the value
    i = len(f_num)
    sum1, sum2 = 0, 0
    exp = 0
    for i in range(len(first) - 1, -1, -1):  # converts the first number to decimal base
        if ('a' <= first[i] <= 'z'):
            num1 = ord(first[i]) - 87
        else:
            num1 = ord(first[i]) - 48
        sum1 += num1 * sys_base ** exp
        exp += 1
    exp = 0
    for i in range(len(second) - 1, -1, -1):  # converts the second number to decimal base
        if ('a' <= second[i] <= 'z'):
            num2 = ord(second[i]) - 87
        else:
            num2 = ord(second[i]) - 48
        sum2 += num2 * sys_base ** exp
        exp += 1
    multiplied = sum1 * sum2  # multiply both numbers together
    return multiplied
def back_conv(sys_base, multiplied, mantissa):  # conversion of decimal number back to the sys_base
    if multiplied == 0:
        print(0)
        return None
    result = []
    storing = False
    integer = int(multiplied)
    for i in range(len(f_num) + len(s_num), -1, -1):
        if (integer // sys_base ** i != 0): # asks if there is any residue after the division with sys_base^i
            if ((integer // sys_base ** i) > 9): # translates the value to the letter
                result.append(chr(int(integer // sys_base ** i) + 87))
            else: # translates the value to the num
                result.append(int(integer // sys_base ** i))
            integer %= sys_base ** i # rewrite the value of integer to the leftover after division
            storing = True
        elif (storing == True): # stores zero if it is required
            result.append(0)
    dot = False
    for i in range(len(result)):  # prints the result in the given sys_base
        if (len(result) == mantissa and not dot):  # prints a dot if the value of mantissa is the length of the whole num
            print("0.", end="")
            dot = True
        if (i == len(result) - 1 and result[i] == 0):
            continue
        else:
            print(result[i], end="")
        if (len(result) - mantissa - 1 == i):  # prints a dot depending on the value of mantissa
            print(".", end="")
    return None
if __name__ == "__main__":
    sys_base = int(input())
    f_num = str(input())
    s_num = str(input())
    f_pos = entry_control(sys_base, f_num)
    first, mantissa1 = conv_mantissa(f_num, f_pos)
    s_pos = entry_control(sys_base, s_num)
    second, mantissa2 = conv_mantissa(s_num, s_pos)
    multiplied = multiply(sys_base, first, second)
    back_conv(sys_base, multiplied, mantissa1 + mantissa2)
