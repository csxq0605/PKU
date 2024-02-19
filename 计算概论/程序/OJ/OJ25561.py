# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 23:51:27 2023

@author: Lenovo
"""

def plans(n,price,count,all_plans,plan):
    if count==n+1:
        all_plans.append(plan[:])
        return
    for i in price[count].keys():
        plan.append(i)
        plans(n,price,count+1,all_plans,plan)
        plan.pop()
    return

def buy(n,m,price,coupon):
    all_plans=[]
    plans(n,price,1,all_plans,[])
    final_price=[]
    for plan in all_plans:
        totals_rsp=[]
        prices=[price[i][plan[i-1]] for i in range(1,n+1)]
        total=sum(prices)
        total-=total//300*50
        for i in range(1,m+1):
            prices_rsp=[price[j+1][plan[j]]for j in range(n) if plan[j] == i]
            totals_rsp.append(sum(prices_rsp))
        store=0
        for total_rsp in totals_rsp:
            store+=1
            discount=0
            for j in coupon[store]:
                if total_rsp>=j[0]:
                    discount=max(j[1],discount)
            total-=discount
        final_price.append(total)
    return min(final_price)

n,m=map(int,input().split())
price,coupon={},{}
for i in range(n):
    price_i={}
    price_raw=list(input().split())
    for j in price_raw:
        price_i[int(list(j.split(':'))[0])]=int(list(j.split(':'))[1])
    price[i+1]=price_i
for i in range(m):
    coupon_i=[]
    coupon_raw=list(input().split())
    for j in range(len(coupon_raw)):
        coupon_i.append(tuple(map(int,coupon_raw[j].split('-'))))
    coupon[i+1]=coupon_i
print(buy(n,m,price,coupon))