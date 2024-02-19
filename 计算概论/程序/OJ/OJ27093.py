# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 22:43:35 2023

@author: Lenovo
"""

import bisect
class Tree:
    def __init__(self,length):
        self.list=[0]*(length+1)
        self.length=length
    
    def lowbit(self,x):
        return x&-x
    
    def update(self,index,value):
        i=index
        while i<self.length+1:
            self.list[i]=max(value,self.list[i])
            i+=self.lowbit(i)
    
    def get_sum(self,index):
        i=index
        ans=0
        while i:
            ans=max(self.list[i],ans)
            i-=self.lowbit(i)
        return ans

n,d=map(int,input().split())
height=list(map(int,input().split()))
h_set=sorted(set(height))
length=len(h_set)
h_dic={v:i for i,v in enumerate(h_set)}
sorted_h,reversed_h=Tree(length),Tree(length)
answer={}
for h in height:
    sorted_index=bisect.bisect_right(h_set, h-d-1)
    reversed_index=length-bisect.bisect_left(h_set, h+d+1)
    sorted_max=sorted_h.get_sum(sorted_index)
    reversed_max=reversed_h.get_sum(reversed_index)
    path=max(sorted_max,reversed_max)+1
    sorted_h.update(h_dic[h]+1,path)
    reversed_h.update(length-h_dic[h],path)
    answer.setdefault(path,[]).append(h)
for path in sorted(answer.keys()):
    for h in sorted(answer[path]):
        print(h,end=" ")