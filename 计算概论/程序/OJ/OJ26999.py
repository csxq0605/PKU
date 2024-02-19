# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 15:59:42 2023

@author: Lenovo
"""

def compute_prefix_function(pat):
    lps=[0]*len(pat)
    length=0
    i=1
    while i<len(pat):
        if pat[i]==pat[length]:
            length+=1
            lps[i]=length
            i+=1
        else:
            if length!=0:
                length=lps[length-1]
            else:
                lps[i]=0
                i+=1
    return lps

def KMP_search(txt,pat):
    lps=compute_prefix_function(pat)
    i=j=0
    res=[]
    while i<len(txt):
        if pat[j]==txt[i]:
            i+=1
            j+=1
        if j==len(pat):
            res.append(i-j)
            j=lps[j-1]
        elif i<len(txt) and pat[j]!=txt[i]:
            if j!=0:
                j=lps[j-1]
            else:
                i+=1
    return res if res else ["no"]

t=int(input())
for _ in range(t):
    txt,pat=input().split()
    print(*KMP_search(txt,pat))