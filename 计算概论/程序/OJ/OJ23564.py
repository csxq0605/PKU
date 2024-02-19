# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 00:07:39 2023

@author: Lenovo
"""

def pFactors(n):
    from math import sqrt
    pFact,limit,check,num={},int(sqrt(n))+1,2,n
    for check in range(2,limit):
        while num%check==0:
            if check in pFact:
                pFact[check]+=1
            else:
                pFact[check]=1
            num /= check
    if num>1:
        pFact[num]=1
    return pFact

n=int(input())
summ=0
for value in pFactors(n).values():
    if value>=2:
        print(0)
        quit()
    summ+=value
if summ%2==0:
    print(1)
else:
    print(-1)