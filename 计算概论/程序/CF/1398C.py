# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 20:15:14 2023

@author: Lenovo
"""

from collections import defaultdict
for _ in range(int(input())):
    n=int(input())
    l=[0]+[int(x) for x in input()]
    summ=ans=0
    dic=defaultdict(int)
    dic[0]+=1
    for i in range(1,n+1):
        summ+=l[i]-1
        ans+=dic[summ]
        dic[summ]+=1
    print(ans)