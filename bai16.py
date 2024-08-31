# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:49:50 2024

@author: phamthiquynhtrang
"""
a= int(input("nhap gio: "))
b= int(input("nhap phut: "))
c= int(input("nhap giay: "))
if 0<a<=12 and 0<=b<=60 and 0<=c<60:  
    print("Tổng giây= ", a*3600+b*60+c)
else:
    print("số không hợp lệ")
