# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 20:59:00 2024

@author: phamthiquynhtrang
"""
n=input("nhap ngay sinh: ")
t=input("nhap tháng sinh: ")
nam=input("nhap nam sinh: ")
print(n + "/"+t+"/"+nam)
namngan=nam[2:]
print(n + "/"+t+"/"+namngan)
ngaynguoc=n[::-1]
thangnguoc=t[::-1]
namnguoc=nam[::-1]
print(ngaynguoc+"/"+thangnguoc+"/"+namnguoc)
namnguocngan=namnguoc[:2]
print(ngaynguoc+"/"+thangnguoc+"/"+namnguocngan)
print(nam + "/"+t+"/"+n)
print(namngan + "/"+t+"/"+n)
print(namnguoc+"/"+thangnguoc+"/"+ngaynguoc)
print(namnguocngan+"/"+thangnguoc+"/"+ngaynguoc)
