# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 10:47:53 2023

@author: Lenovo
"""

def encrypt(line):
    length=len(line)
    ans=""
    for i in range(length):
        tmp=ord(line[i])+int(decode[i%7])
        if tmp>122:
            tmp=tmp%122+31
        ans+=chr(tmp)
    return ans

def decrypt(line):
    length=len(line)
    ans=""
    for i in range(length):
        tmp=ord(line[i])-int(decode[i%7])
        if tmp<32:
            tmp=122-31%tmp
        ans+=chr(tmp)
    return ans

decode="4962873"
line=input()
ans1=encrypt(line)
ans2=decrypt(ans1)
print(ans1)
print(ans2)