# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 22:10:07 2023

@author: Lenovo
"""

def calculate(j): #计算更换湖泊时可钓鱼的数量
    if float(interval)>=f[lake[0]]/d[lake[0]]:
        return 0
    else:
        fi=f[lake[0]]-interval*d[lake[0]]
        di=d[lake[0]]
        num=fi
        for _ in range(t[j]):
            fi-=di
            if fi>0:
                num+=fi
            else:
                return num
        return num

def check(): #寻找是否有最好的lake供垂钓
    global lake
    time=totaltime-interval   
    numall=0
    j=lake[0]
    flag,sign=True,True
    if d[lake[0]]==0:
        return False
    while flag and j<n-1:
        numall+=calculate(j)    
        j+=1
        time-=t[j-1]
        if numall<f[j] and time>0:
            lake[1]=j
            sign=False
        elif time<=0:
            flag=False
    return sign

def count(interval): #计算一段时间内的钓鱼数量  
    if d[lake[0]]==0:
        return f[lake[0]]*interval
    else:
        if float(interval)>=f[lake[0]]/d[lake[0]]:
            return (f[lake[0]]+f[lake[0]]%d[lake[0]])*(f[lake[0]]//d[lake[0]]+1)//2
        else:
            return (f[lake[0]]*2-d[lake[0]]*interval)*interval//2          

while True:
    n=int(input())
    if n==0:
        break
    totaltime=int(input())*12
    f=list(map(int,input().split()))
    d=list(map(int,input().split()))
    t=list(map(int,input().split()))
    times=["0"]*n
    lake,totalnum=[0,0],0
    interval=totaltime
    while totaltime>0:
        if check() and interval>=0:
            interval-=1
        elif check() and interval<0:
            times[lake[0]]=str(totaltime*5)
            totalnum+=count(totaltime)
            totaltime=0
        else:
            times[lake[0]]=str(interval*5)
            totalnum+=count(interval)
            totaltime-=interval
            for i in range(lake[0],lake[1]):
                totaltime-=t[i]
            interval=totaltime
            lake[0]=lake[1]
    print(", ".join(times))
    print(f"Number of fish expected: {totalnum}")
    print()