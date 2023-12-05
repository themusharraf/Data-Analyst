"""
2.1.1. N-o'lchamli massiv (array)larga ishlov berish
Numpyda massiv yaratishning eng oson yo'llaridan biri bu array
funksiyasi yordamida amalga oshiriladi. Va ushbu funksiya har
 qanday turdagi ketma-ket ma'lumotlarni qabul qilib, uni yangi
 Numpy arrayiga o'girib beradi.
"""
import numpy as np

data1 = [3.5, 5, 6, 2]  # list
arr1 = np.array(data1)  # array1
print(arr1)
array = [3.5, 5., 6., 2.]
data2 = (4, 5, 3.2, 7)  # tuple
arr2 = np.array(data2)
print(arr2)
