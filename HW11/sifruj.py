#!/usr/bin/env python3
# easy variant of the task No.11
# GNU General Public License v3.0
import sys
def encrypt(n,e,msg):
    encr_chars=[]
    for i in range(0,len(msg),4): 
        num=0
        for j in range(4): # calculates num for 4 chars
            if i+j>=len(msg): # if the input message does not have the number of characters %4, the rest is filled with the value zero
                char=0
            else:
                char=ord(msg[i+j])
            num=num*256+char
        cipher=pow(num,e,n) # encrypts the num using key; (num**e)%n is MUCH slower
        #cipher=(num**e)%n
        encr_chars.append(cipher)
    return encr_chars
if __name__ == "__main__":
    n=int(sys.argv[1]) # load public key
    e=int(sys.argv[2])
    msg=input() # loads msg to encrypt
    encr_chars=encrypt(n,e,msg) # returns encrypted msg
    print(*encr_chars,sep=" ")