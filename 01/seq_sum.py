#difficult variant of the task No.1
#GNU General Public License v3.0
def find_prime_nums(number): #func for finding prime numbers
    not_prime=True
    if(number!=1 and number!=0 and number!=2):
        for j in range (2, abs(number)):
            if((number%j)==0):
                not_prime=True
                break
            else:
                not_prime=False
    elif(number==2):
        not_prime=False
    else:
        not_prime=True
    return not_prime
def saving(old_count,count,old_sum,sum): #func for finding "stronger" sequences
    if ((count>old_count) or (count==old_count and sum>old_sum)):
        old_count=count
        old_sum=sum
    return old_count,count,old_sum,sum
nums=list(map(int, input().split())) #splits the input into an array, the separator is space
old_count,count=0,0
old_sum,sum=0,0
old_num=None #None, bcs I needed some neutral value the input never reaches, but at the same time can be compared
for i in range (0,len(nums)):
    if (find_prime_nums(abs(nums[i])) and (old_num==None or old_num>nums[i])): #looks for a matching number, which it then adds to the sequence
        count+=1
        sum+=nums[i]
        old_num=nums[i]
    else:
        old_count,count,old_sum,sum=saving(old_count,count,old_sum,sum) #evaluates which sequence is stronger
        if find_prime_nums(abs(nums[i])): #storing the last number that meets the conditions and also ends the series
            count=1
            sum=nums[i]
            old_num=nums[i]
        else:
            count=0
            sum=0
            old_num=None
old_count,count,old_sum,sum=saving(old_count,count,old_sum,sum) #evaluates which sequence is stronger after the last number
print(str(old_count)+"\n"+str(old_sum)) #prints output
