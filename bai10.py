# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:42:35 2024

@author: phamthiquynhtrang
"""
a=int(input("nhap 4 so xe : "))
nguyen1 = a //1000
du1 = a%1000
nguyen2 = du1 // 100
du2 = du1 %100
nguyen3 = du2 // 10
du3 = du2 %10
nguyen4 = du3
t=nguyen1 +nguyen2 +nguyen3 +nguyen4
print("số nút của bạn là: ",t)