# 4_Divisors
try:
    number = int(input("Input a number to check divisors\n"))
except ValueError:
    print(f"Fuck you")
    quit()

result = []

for i in range(1,number+1):
    if number % i == 0:
        result.append(i)

print(result)
