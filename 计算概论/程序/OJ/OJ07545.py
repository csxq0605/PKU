# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 23:34:40 2023

@author: Lenovo
"""

m,n=map(int,input().split())
martix=[list(map(int,input().strip().split()))for i in range(m)]
cnt_x,cnt_y,dx,dy=0,0,1,0
cnt_n,cnt_s,cnt_e,cnt_w=0,m-1,n-1,0
for i in range(1,m*n+1):
    print(martix[cnt_y][cnt_x])
    cnt_x+=dx
    cnt_y+=dy
    if dx==1 and dy==0 and cnt_x==cnt_e and cnt_y==cnt_n:
        dx,dy=0,1
        cnt_n+=1
    elif dx==0 and dy==1 and cnt_x==cnt_e and cnt_y==cnt_s:
        dx,dy=-1,0
        cnt_e-=1
    elif dx==-1 and dy==0 and cnt_x==cnt_w and cnt_y==cnt_s:
        dx,dy=0,-1
        cnt_s-=1
    elif dx==0 and dy==-1 and cnt_x==cnt_w and cnt_y==cnt_n:
        dx,dy=1,0
        cnt_w+=1