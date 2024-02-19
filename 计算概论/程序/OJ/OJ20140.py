# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 16:26:24 2023

@author: Lenovo
"""

def search(string):
    for _ in range(len(string)):
        if ord(string[_])>=97:
            num=int(string[:_])
            string=string[_:]*num
            return string
            
s=list(input())
l=[0]*len(s)
cnt=0
for i in range(len(s)):
    if s[i]=="[":
        s[i]=""
        l[cnt]=i
        cnt+=1
    elif s[i]=="]":
        s[i]=""
        cnt-=1
        string="".join(s[l[cnt]+1:i])
        s[l[cnt]]=search(string)
        for _ in range(l[cnt]+1,i):
            s[_]=""
print("".join(s))