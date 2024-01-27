# 2_Odd_Or_Even
try:
    number = int(input("Enter the number:\n"))
except ValueError:
    print(f"Please, enter an integer")
    quit()

if number % 4 == 0:
    print("The number you've chosen is EVEN, and its a multiple of 4")
elif number % 2 == 0:
    print("The number you've chosen is EVEN")
else:
    print("The number you've chosen is ODD")