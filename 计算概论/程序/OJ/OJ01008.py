# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:31:33 2023

@author: Lenovo
"""

n=int(input())
days=[]
for i in range(n):
    day=input()
    d=day.replace(".","")
    days.append(list(d.split()))
dic_Haab={"pop":0,"no":1,"zip":2,"zotz":3,"tzec":4,"xul":5,"yoxkin":6,"mol":7,"chen":8,"yax":9,"zac":10,"ceh":11,"mac":12,"kankin":13,"muan":14,"pax":15,"koyab":16,"cumhu":17,"uayet":18}
dic_Tzolkin={1:"imix",2:"ik",3:"akbal",4:"kan",5:"chicchan",6:"cimi",7:"manik",8:"lamat",9:"muluk",10:"ok",11:"chuen",12:"eb",13:"ben",14:"ix",15:"mem",16:"cib",17:"caban",18:"eznab",19:"canac",20:"ahau"}
day_new=[n]
for i in days:
    date=int(i[0])+dic_Haab[i[1]]*20+int(i[2])*365
    year=date//260
    month=dic_Tzolkin[date%260%20+1]
    day=date%260%13+1
    date=str(day)+" "+month+" "+str(year)
    day_new.append(date)
for i in range(n+1):
    print(day_new[i])