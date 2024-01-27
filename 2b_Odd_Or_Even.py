# 2_Odd_Or_Even
try:
    number = int(input("Enter the number you'd like to check\n"))
    check = int(input("Enter the divisor of your number to check\n"))
except ValueError:
    print(f"You've entered other content than integers")
    quit()


if number % check == 0:
    print(f"{check} is the divisor of {number}")
else:
    print(f"{number} isn't a multiple of {check}")