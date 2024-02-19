# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 09:22:47 2023

@author: Lenovo
"""

l=list(map(str,input().split()))
dic={"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"ten":10,"eleven":11,"twelve":12,"thirteen":13,"fourteen":14,"fifteen":15,"sixteen":16,"seventeen":17,"eighteen":18,"nineteen":19,"twenty":20,"thirty":30,"forty":40,"fifty":50,"sixty":60,"seventy":70,"eighty":80,"ninety":90,"hundred":100,"thousand":1000,"million":1000000}
sign=1
if l[0]=="negative":
    sign=-1
    del l[0]
ans=tmp=0
for word in l:
    if word=="thousand" or word=="million":
        ans+=tmp*dic[word]
        tmp=0
    elif word=="hundred":
        tmp*=dic[word]
    else:
        tmp+=dic[word]
ans+=tmp
print(sign*ans)