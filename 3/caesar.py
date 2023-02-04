#easy variant of the task No.3
#GNU General Public License v3.0
def gcd(f_num, s_num):
    while(f_num != s_num):
        if(f_num>s_num):
            f_num= f_num - s_num
        else:
            s_num= s_num - f_num
    return int(f_num)
num_rows=int(input())
input_num=[]
symbol=[]
for i in range(num_rows):
    input_num=(list(map(int, input().split())))
    symbol.append(gcd(input_num[0], input_num[1]))
for j in range (num_rows):
    print(chr(symbol[j]), end="")
