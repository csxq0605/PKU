# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 18:21:53 2023

@author: Lenovo
"""

m,s,c=map(int,input().split())
if m>=c:
    print(c)
    quit()
l=[]
for i in range(c):
    l.append(int(input()))
l.sort()
d=[l[i+1]-l[i] for i in range(c-1)]
d.sort(reverse=True)
delete=sum(d[0:m-1])
print(l[-1]-l[0]-delete+m)