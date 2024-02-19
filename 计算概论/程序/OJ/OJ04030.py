# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 11:00:19 2023

@author: Lenovo
"""

word=" "+input().lower()+" "
article=" "+input().lower()+" "
position=article.find(word)
if position==-1:
    print(-1)
else:
    words=list(article.split())
    num=words.count(word[1:len(word)-1])
    print(num,position)