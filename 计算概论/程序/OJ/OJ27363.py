# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 15:26:15 2023

@author: Lenovo
"""

from collections import defaultdict
n=int(input())
l=list(map(int,input().split()))
ans,cnt=0,1#结果，在队列中的指针
flag=True#标记是否合规
queue=[0]#队列，目前正在涂色的非间断区域
dic=defaultdict(int)#数字在队列内所处的位置记录
c=defaultdict(int)#记录每个数字可能所在的层数，从上到下，从0开始
s=set()#对数字去重，如果在前面的间断区域内已经出现而再次出现则不合规
for num in l:
    if num in s:#不合规
        flag=False
        break
    if dic[num] and cnt==dic[num]+1: #连续涂色
        continue
    elif dic[num] and cnt>dic[num]+1:#出现间断区域
        ceil=0
        for j in range(cnt-1,dic[num],-1):#在这个间断区域内
            p=queue.pop()#每个涂色数字
            if p==0:#区间内不可能出现0
                flag=False
                break
            s.add(p)#已经出现则只能在这个间断区域内出现
            ceil=max(c[p],ceil)#找到区域两端数字所处的最大层数
        cnt=dic[num]+1#指针初始化
        c[num]=max(c[num],(ceil+1))#将这个层数记录
    else:#还没有出现间断区域
        queue.append(num)#入队
        dic[num]=cnt #记录数字位置
        cnt+=1
for v in c.values(): #找到所有数字中所处的最大层数
    ans=max(ans,v)
l_set=set(l)
if l_set=={0}:
    ans=-1#仅有0，不涂色 
print(ans+1 if flag else -1)#最大层数数字下还有一层0，故加一