# 5_List_Overlap
import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common = []
a, b = set(a), set(b)

for number in a:
    if number in b:
        common.append(number)

print(common)
