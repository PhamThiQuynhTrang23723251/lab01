# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:49:57 2024

@author: phamthiquynhtrang
"""
a=int(input("nhap a: "))
b=int(input("nhap b: "))
bieuthuc=((a+b)/(a**(1/3)+b**(1/3))/(a**(1/3)-b**(1/3))**2)
print("ket qua: ",bieuthuc)