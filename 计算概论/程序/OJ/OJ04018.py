# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 13:48:03 2023

@author: Lenovo
"""

while True:
    try:
        str1,str2=input().split()
        len1,len2=len(str1),len(str2)
        dp = [[0]*(len2+1) for _ in range(len1+1)]
        for i in range(len1):
            for j in range(len2):
                if str1[i]==str2[j]:
                    dp[i+1][j+1]=dp[i][j]+1
                else:
                    dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
        if dp[len1][len2]==len1:
            print("Yes")
        else:
            print("No")
    except EOFError:
        break