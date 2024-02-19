# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 16:59:14 2023

@author: Lenovo
"""

import re
while True:
    try:
        s=input()
        m="<([A-Za-z]{1,5})>(.*)</\\1>"
        lst=re.findall(m,s)
        v=0
        if lst:
            for i in lst:
                s=i[1]
                m=".<([A-Za-z]{1,5})>(.*?)</\\1>."
                nlst=re.findall(m,s)
                if nlst:
                    for j in nlst:
                        s=j[1]
                        m="(\d+)"
                        result=re.findall(m,s)
                        if result:
                            for n in result:
                                if n=='0' or (len(n)<5 and n[0]!='0'):
                                    print(n,end=" ")
                                    v=1
        if v==1:
            print("")
        else:
            print("NONE")
    except:
        break