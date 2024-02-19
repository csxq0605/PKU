# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 09:27:51 2023

@author: Lenovo
"""

def change(line1,line2,line3):
    if m<=2:
        line2_new=line2
    else:
        line2_new=[line2[0],line2[-1]]
        for i in range(1,m-1):
            average=round((line1[i]+line2[i-1]+line2[i]+line2[i+1]+line3[i])/5)
            line2_new.insert(i,int(average))
    return line2_new

n,m=map(int,input().split())
photo=[]
for i in range(n):
    photo.append([int(x) for x in input().split()])
if n<=2:
    photo_new=photo
else:
    photo_new=[photo[0],photo[-1]]
    for i in range(1,n-1):
        photo_new.insert(i,change(photo[i-1],photo[i],photo[i+1]))
for l in photo_new:
    l_n=[str(i) for i in l]
    print(" ".join(l_n))
