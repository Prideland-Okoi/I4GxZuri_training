import random
from random import choice

print("=====Welcome to Rock, Paper, Scissors Game, Build with Python Language=====")
print("\n")
name = input("Player inputs name")
print(name, "You are welcome!")
list=("R","P","S")

def checkforwinner(name, computer):
    if (name=="R" and computer=="P"):
        print("You chose Rock, Computer chose Paper: Paper covers Rock. You lost")
        return play_again()
    elif (name=="R" and computer=="S"):
        print("You chose Rock, Computer chose Scisdors: Rock smashes Scissors. Congrats!!! You won")
        return play_again()
    elif (name=="S" and computer=="P"):
        print("You chose Scissors, Computer chose Paper: Scissors cut Paper. Congrats!!! You won")
        return play_again()
    elif (name="S" and computer=="R"):
        print("You chose Scissors, Computer chose Rock. Rock smashes Scissors. You lost")
        return play_again()
    elif (name=="P" and computer=="R"):
        print("You chose Paper, Computer chose Rock. Paper covers Rock. Congrats!!! You won")
        return play_again()
    elif (name=="P" and computer=="S"):
        print("You chose Paper, Computer chose Scissors. Scissors cuts paper. You lost")
        return play_again()

While True:
    user=input("\nPick a hand. R for Rock, P for Paper, S for Scissors:  ")
    if ( name=="R" or name="P" or name="S"):
        break
    else:
        print("Invalid input, Try again")
        return play_again()

def play_again():
    play_again= input("Clearly understands the instruction, want to try again, 
