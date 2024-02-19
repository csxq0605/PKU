# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 15:53:03 2023

@author: Lenovo
"""

from itertools import product
import copy
martix=[[0]*8]+[[0]+list(map(int,input().split()))+[0] for i in range(5)]+[[0]*8]
for cases in product([0,1],repeat=6):
    martixcopy=copy.deepcopy(martix)
    ans=[list(cases)]
    for i in range(1,6):
        for j in range(1,7):
            if ans[i-1][j-1]:
                martixcopy[i][j]=(martixcopy[i][j]+1)%2
                martixcopy[i][j-1]=(martixcopy[i][j-1]+1)%2
                martixcopy[i][j+1]=(martixcopy[i][j+1]+1)%2
                martixcopy[i+1][j]=(martixcopy[i+1][j]+1)%2
        ans.append(martixcopy[i][1:7])
    if martixcopy[5][1:7]==[0,0,0,0,0,0]:
        for line in ans[0:-1]:
            print(*line)