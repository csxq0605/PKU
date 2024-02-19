# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 15:39:10 2023

@author: Lenovo
"""

def divide(nums):
    ans=0
    if nums[0]>0:
        return ans
    for i in range(len(nums)-2):
        if nums[i]>0:
            break
        if i>=1 and nums[i]==nums[i-1]:
            continue
        l,r=i+1,len(nums)-1
        while l<r:
            summ=nums[i]+nums[l]+nums[r]
            if summ==0:
                ans+=1
                l+=1
                r-=1
                while l<r and nums[l]==nums[l-1]:
                    l+=1
                while l<r and nums[r]==nums[r+1]:
                    r-=1
            elif summ<0:
                l+=1
                while l<r and nums[l-1]==nums[l]:
                    l+=1
            else:
                r-=1
                while l<r and nums[r+1]==nums[r]:
                    r-=1
    return ans

line=list(map(int,input().split()))
line.sort()
ans=divide(line)
print(ans)