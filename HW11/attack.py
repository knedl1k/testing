#!/usr/bin/env python3
# difficult variant of the task No.11
# GNU General Public License v3.0
import sys
from math import gcd
def decrypt(n, e, encr_chars):
    decr_chars = []
    for cipher in encr_chars:
        num = pow(cipher, e, n)
        decr_char = ""
        for i in range(4):
            char = num % 256
            decr_char = chr(char) + decr_char
            num //= 256
        decr_chars.append(decr_char)
    return "".join(decr_chars)
if __name__ == "__main__":
    key=["Tento", "predmet", "proste", "nejlepsi", "genialni"]
    n = int(sys.argv[1])
    encr_chars =[int(x) for x in input().split()]
    phi_n = n - 1
    for e in range(2 ** 18, 2 ** 20):
        if gcd(e, n):
            decr_msg = decrypt(n, e, encr_chars)
            for word in key:
                if word in decr_msg:
                    print(decr_msg)
                    break
