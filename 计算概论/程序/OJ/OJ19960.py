# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 11:02:10 2023

@author: Lenovo
"""

left=[list(map(int,input().split())) for _ in range(6)]
mid=[list(map(int,input().split())) for _ in range(6)]
right=[list(map(int,input().split())) for _ in range(6)]
reflect=[list(map(int,input().split())) for _ in range(3)]
decode=list("oabcdef")
line=input()
lcnt=mcnt=rcnt=0
ans=""
for i in line:
    index=decode.index(i)
    for pair in left:
        if pair[0]==index:
            index=pair[1]
            break
    for pair in mid:
        if pair[0]==index:
            index=pair[1]
            break
    for pair in right:
        if pair[0]==index:
            index=pair[1]
            break
    for pair in reflect:
        if pair[0]==index:
            index=pair[1]
            break
        if pair[1]==index:
            index=pair[0]
            break
    for pair in right:
        if pair[1]==index:
            index=pair[0]
            break
    for pair in mid:
        if pair[1]==index:
            index=pair[0]
            break
    for pair in left:
        if pair[1]==index:
            index=pair[0]
            break
    ans+=decode[index]
    lcnt+=1
    for pair in left:
        pair[0]=pair[0]%6+1
        pair[1]=pair[1]%6+1
    if lcnt==6:
        lcnt=0
        mcnt+=1
        for pair in mid:
            pair[0]=pair[0]%6+1
            pair[1]=pair[1]%6+1
    if mcnt==6:
        mcnt=0
        rcnt+=1
        for pair in right:
            pair[0]=pair[0]%6+1
            pair[1]=pair[1]%6+1
print(ans)        