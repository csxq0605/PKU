# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 10:09:20 2023

@author: Lenovo
"""

class Point:
    def __init__(self, x, y, m):
        self.x = x
        self.y = y
        self.m = m

maze=[[0]*1025 for _ in range(1025)]
d=int(input())
n=int(input())
p=[Point(0,0,0)for _ in range(n)]
for i in range(n):
    p[i].x,p[i].y,p[i].m=map(int,input().split())
np=ans=0
for i in range(n):
    for row in range(max(0,p[i].x-d),min(1025,p[i].x+d+1)):
        for col in range(max(0,p[i].y-d),min(1025,p[i].y+d+1)):
            maze[row][col]+=p[i].m
            if ans<maze[row][col]:
                ans=maze[row][col]
                np=1
            elif ans==maze[row][col]:
                np+=1
print(f"{np} {ans}")