# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:34:37 2023

@author: Lenovo
"""

n,a,b=map(int,input().split())
temp=[1,n]
for bb in range(n,1,-1):
    for aa in range(bb-1,0,-1):
      if aa*temp[1]>=bb*temp[0] and aa*b<bb*a:
          temp=[aa,bb]    
print(temp[0],temp[1])