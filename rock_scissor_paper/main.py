import random
from random import choice

while True:
    print("=====Rock, Paper, ScissorsGame: Build with Python Language=====")
    print("\n")

    name = input("Player please enter you name:\n")
    print("Your are welcome", name, "!")
    print("\n")


    user_pick = input("Please select options in capital letters: Enter R for Rock, P for  Paper or S for Scissors:\n")

    if user_pick == "R" or user_pick == "P" or user_pick == "S":
        print(name, "Your choice is been processed. ")
    else:
        user_pick != "R" or user_pick != "P" or user_pick != "S"
        print(name, "You have not clearly followed the instruction\n")
        print(name, "you inputted an invalid letter\n")

    #Computer's Choices
    list= ["R","P","S"]
    computer_Choice = random.choice(list)
    if computer_Choice == 'R':
        computer_Choice = "R"
        print(f"Computer chooses {computer_Choice}...")
    if computer_Choice == 'P':
        computer_Choice = "P"
        print(f"Computer chooses {computer_Choice}...")
    if computer_Choice == 'S':
        computer_Choice = "S"
        print(f"Computer chooses {computer_Choice}...")


    if user_pick == computer_Choice:
        print("Try Again!! You and the Computer picked the same thing")

    #How I can loose to the CPU
    if user_pick == "R" and computer_Choice == "P":
        print("[Paper covers Rock]")
        print("oops!!! Computer WINS!!!")
    if user_pick == "P" and computer_Choice == "R":
        print("[Paper covers Rock]")
        print(f"Congrats!!! {name} WINS!!!")

    if user_pick == "S" and computer_Choice == "R":
        print("[Rock Smashes Scissors]")
        print("Oops!!! Computer WINS!!!")
    if user_pick == "R" and computer_Choice == "S":
        print("[Rock smashes Scissors]")
        print(f"Congrats!!! {name} WINS!!!")

    if user_pick == "P" and computer_Choice == "S":
        print("[Scissors cut Paper]")
        print("Oops!!! Computer WINS!!!")
    if user_pick == "S" and computer_Choice == "P":
        print("[Scissors cut Paper]")
        print(f"Congrats!!! {name} WINS!!!")

    exit = input("\nWould you like to play game? Y/N  ")
    if exit=="N":
        break
