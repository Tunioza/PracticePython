# 16_Password_Generator
import string
import random
def password_gen(level):
    if level == "weak":
        return "password123"

    if level == "medium":
        return random.choices(string.ascii_letters, k=10)

    if level == "hard":
        return random.choices(string.printable, k=16)


choice = input("Would you like weak, medium or hard password?\n")
purpose = input("What is the purpose of this password?\n")

password = "".join(str(x) for x in (password_gen(choice)))
print(password)


with open("passwords.txt", "a") as f:
    f.write(f"{str(password)} - {purpose}\n")

