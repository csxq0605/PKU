# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 23:25:01 2023

@author: Lenovo
"""

for _ in range(int(input())):
    n=int(input())
    x=y=z=0
    face,left,verdical=0,4,2
    for i in range(n):
        function,d=input().split()
        if function=="left":
            face,left=left,(face+3)%6
        elif function=="back":
            face=(face+3)%6
            left=(left+3)%6
        elif function=="right":
            left,face=face,(left+3)%6
        elif function=="up":
            face,verdical=verdical,(face+3)%6
        elif function=="down":
            verdical,face=face,(verdical+3)%6
        if face==0:
            x+=int(d)
        elif face==1:
            y+=int(d)
        elif face==2:
            z+=int(d)
        elif face==3:
            x-=int(d)
        elif face==4:
            y-=int(d)
        else:
            z-=int(d)
    print(x,y,z,face)