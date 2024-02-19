# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 13:17:28 2023

@author: Lenovo
"""

import heapq
class Cow:
    def __init__(self,start,end,No):
        self.start=start
        self.end=end
        self.No=No

def solve(cows):
    cows.sort(key=lambda x:x.start)
    heap=[]
    k=0
    res=[0]*len(cows)
    for cow in cows:
        if heap and heap[0][0]<cow.start:
            _,No = heapq.heappop(heap)
            res[cow.No]=res[No]
        else:
            k+=1
            res[cow.No]=k
        heapq.heappush(heap,(cow.end,cow.No))
    print(k)
    for num in res:
        print(num)

def main():
    n=int(input())
    cows=[]
    for i in range(n):
        start,end=map(int,input().split())
        cows.append(Cow(start,end,i))
    solve(cows)

if __name__ == "__main__":
    main()