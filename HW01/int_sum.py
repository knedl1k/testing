#easy variant of the task No.1
#GNU General Public License v3.0
f_num=int(input())
s_num=int(input())
output=0
if(f_num<=s_num):
    for i in range (f_num, s_num + 1):
        output+= i ** 3
else:
    for i in range (s_num, f_num + 1):
        output+= i ** 3
print(str(output))#prints a sum of a cubic values in range from the smallest number included to the biggest number included
