# 11_Check_Primality_Functions

def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

candidate = int(input("Enter the number that you'd love to check\n"))
print(is_prime(candidate))

