# 1_Character_Input
import datetime
try:
    name, age = input("What is your name?\n"), int(input("How old are you?\n"))
except ValueError:
    print("You entered age in other medium than numbers")
    quit()

year = str(datetime.datetime.now())
year = int(year[0:4])

print(f"Hey {name}, you are {age} now, but in {100 - age + year} years you will be 100 year old!")