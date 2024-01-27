# 8_Rock_Paper_Scissors
import random


def win(u, ai):
    if u == "paper" and ai == "rock" or u == "scissors" and ai == "paper" or u == "rock" and ai == "scissors":
        return 1

    elif u == ai:
        return 3

    else:
        return 0


while True:
    choices = ["rock", "paper", "scissors"]

    secret = random.choice(choices)
    while True:
        player = input("What is your weapon of choice? Rock, Paper or Scissors?\n").lower()
        if player not in choices:
            print("Wrong input")
            continue
        break

    verdict = win(player, secret)

    if verdict == 1:
        print("You won!")
    elif verdict == 3:
        print("Tie!")
    else:
        print("You lost!")

    restart = input("Wanna play again buddy? y/n\n").lower()
    if restart == "y":
        print("Here we go again")
        continue
    elif restart == "n":
        print("Thanks for the game!")
        break
    else:
        print("I'll take it as a no")
        break




