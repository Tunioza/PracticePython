# 3_List_Less_Than_Ten
try:
    user_choice = int(input("Enter a number for the list:\n"))
except ValueError:
    print(f"Fuck you")
    quit()

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
result = [x for x in a if x < user_choice]

print(result)