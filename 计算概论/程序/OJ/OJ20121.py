# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 10:25:18 2023

@author: Lenovo
"""

n=int(input())
martix=[list(map(int,input().split())) for i in range(n)]
cnt_x,cnt_y,dx,dy=0,0,1,0
cnt_n,cnt_s,cnt_e,cnt_w=0,n-1,n-1,0
ans=[]
for i in range(1,n*n+1):
    ans.append(str(martix[cnt_y][cnt_x]))
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
print("".join(ans))