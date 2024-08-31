# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:56:43 2024

@author: phamthiquynhtrang
"""
a=float(input("nhap so a: "))
b=float(input("nhap so b: "))
if a==0 :
    if b==0:
        print("phuong trinh vo so nghiem")
    else:
        print("phuong trinh vo nghiem")
else:
    x=-b/a
    print("nghiem cua phuong trinh la: ",x)
    