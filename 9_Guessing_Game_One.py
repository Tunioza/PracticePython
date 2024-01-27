# 9_Guessing_Game_One
import random
secret = random.randint(1,10)
i = 0
while True:
    try:
        player = int(input("Guess the number!\n"))
    except ValueError:
        ex = input("Do you really wanna exit? y/n\n").lower()

        if ex == "y":
            print("Thanks for the game")
            print(f"You tried {i} times!")
            break
        else:
            continue


    if i == 10:
        print("Bitch you trippin'")
        print("Uninstalling system32 from your computer")
        print("Bye")
        break

    if player == secret:
        print("You won!")
        print(f"You guessed it in {i} tries!")
        break
    elif player > secret:
        print("Secret number is lower")
    else:
        print("Secret number is bigger")
    i += 1

