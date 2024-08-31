# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 20:25:12 2024

@author: phamthiquynhtrang
"""
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))
temp = 0
if a > b:
    temp = a
    a = b
    b = temp
if a > c:
    temp = a
    a = c
    c = temp
if b > c:
    temp = b
    b = c
    c = temp
print("Thứ tự tăng dần: ", a, b, c)
n = int(input("Nhập số nguyên N có 2 chữ số trở lên : "))
if n >= 10:
    chuso = [int(x) for x in str(n)]
    chuso.sort()
    n_moi = int("".join(map(str, chuso)))
    print("Số có các chữ số theo thứ tự tăng dần: ", n_moi)
else:
    print("số không hợp lệ")
        
