# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 17:46:50 2023

@author: Lenovo
"""

n=int(input())
words=[input() for i in range(n)]
words.sort()
fm,lm=words[n//2-1],words[n//2]
ans,cur,flag="",0,False
while cur<len(fm):
    for i in range(26):    
        tmp=ans+chr(65+i)
        if fm<=tmp<lm:
            ans=tmp
            flag=True
            break
    if flag:
       break
    ans+=fm[cur]
    cur+=1
print(ans)