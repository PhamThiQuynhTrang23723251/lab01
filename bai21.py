# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 20:18:40 2024

@author: 
"""
def doc_so(so):
  so_chu = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
  if 0 <= so <= 9:
    return so_chu[so]
  else:
    return ( "Không đọc được")
so_nhap= int(input("Nhập một số: "))
print(doc_so(so_nhap))
