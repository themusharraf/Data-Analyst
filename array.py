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

arr9 = np.random.randint(5, size=(2, 4))  # (2, 4) o'lchamli va max qiymati 5 gacha bo'lgan int sonlar
print(arr9)

arr6 = np.arange(4, 20, 2)  # 4 dan 20 gacha bo'lgan qiymatlarni 2 qadam bilan massivga joylab beradi
print(arr6)

arr5 = np.ones((2, 4))  # barcha elementlari 1 ga teng bo'lgan (2, 4)
print(arr5)

arr4 = np.zeros((2, 4))  # barcha elemtlari 0 ga teng bo'lgan (2, 4)
print(arr4)
