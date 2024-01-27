# 13_Fibonacci
user_input = int(input("Enter number to be a border of fibonacci sequence\n"))
if user_input < 1:
    quit()
def fibo(user_input):
    prv1 = 0
    prv2 = 1
    result = None
    print(0)
    for i in range(0, user_input-1):
        result = prv1 + prv2
        prv2 = prv1
        prv1 = result
        print(result)

fibo(user_input)