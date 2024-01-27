# 12_List_Ends

a = [5, 10, 15, 20, 25]
b = [x for x in a if x == a[0] or x == a[-1]]

print(b)