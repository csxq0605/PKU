# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 12:45:30 2023

@author: Lenovo
"""

def decode(string,cnt):
    string=string[::-1]
    ans=""
    for s in string:
        if "A"<=s<="Z" and 65<=ord(s)-cnt<=90:
            ans+=chr(ord(s)-cnt)
        elif "A"<=s<="Z" and ord(s)-cnt<65:
            ans+=chr(ord(s)+26-cnt)
        elif "a"<=s<="z" and 97<=ord(s)-cnt<=122:
            ans+=chr(ord(s)-cnt)
        else:
            ans+=chr(ord(s)+26-cnt)
    return ans

while True:
    try:
        s=input()
    except EOFError:
        break
    ans=tmp=""
    cnt=0
    for st in s:
        if "A"<=st<="Z" or "a"<=st<="z":
            tmp+=st
        else:
            if tmp:
                cnt+=1
                ans+=decode(tmp,cnt)
                tmp=""
            ans+=st
    if tmp:
        cnt+=1
        ans+=decode(tmp,cnt)
    print(ans)