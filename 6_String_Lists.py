# 6_String_Lists

words = input("Enter a sentence\n").lower().replace(" ", "")

if words == words[::-1]:
    print("It is a palindrome")
else:
    print("Fuck you")
