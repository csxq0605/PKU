# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 16:18:39 2023

@author: Lenovo
"""

def isMatch(s,p):
    slen=len(s)
    plen=len(p)
    s_idx=0
    p_idx=0
    p_idx2=-1
    s_idx2=-1
    while s_idx<slen:
        if p_idx<plen and (p[p_idx]=='?' or p[p_idx]==s[s_idx]):
            s_idx+=1
            p_idx+=1
        elif p_idx<plen and p[p_idx]=='*':
            p_idx2=p_idx
            s_idx2=s_idx
            p_idx+=1
        elif p_idx2==-1:
            return False
        else:
            p_idx=p_idx2+1
            s_idx=s_idx2+1
            s_idx2+=1
    while p_idx<plen:
        if p[p_idx]!='*':
            return False
        p_idx+=1
    return True

n=int(input())
for i in range(n):
    s=input()
    p=input()
    result=isMatch(s,p)
    if result:    
        print("yes")
    else:
        print("no")