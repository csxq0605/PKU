# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 14:04:53 2023

@author: Lenovo
"""

line=input()
dic={"R":0,"B":1}
line=[dic[i] for i in line]
ans,t=0,1
for i in range(len(line)-1,-1,-1):
    if line[i]==t and line[i-1]!=t:
        ans+=1
    if line[i]==t and line[i-1]==t:
        t=(t+1)%2
        ans+=1
print(ans)