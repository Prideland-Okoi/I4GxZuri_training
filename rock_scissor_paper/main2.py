import random
from random import choices

def welcome_message():
    print("You are welcome to Rock-Paper-Scissor Game")
welcome_message()


def game_start():
    while True:
        computer_list = ["R","P","S"]

        computer = random.choices(computer_list)
        player_name = input("Please select your choice:R for rock, P for paper, or S for scissors?: ").upper()

        if player_name == computer:
            print("computer: ",computer)
            print("player: ",player_name)
            print("Tie!")

        elif player_name == "R":
            if computer == "P":
                print("computer: ", computer)
                print("player: ", player_name)
                print("You lose!")
            if computer == "S":
                print("computer: ", computer)
                print("player: ", player_name)
                print("You win!")

        elif player_name == "S":
            if computer_list == "R":
                print("computer: ", computer)
                print("player: ", player_name)
                print("You lose!")
            if computer == "P":
                print("computer: ", computer)
                print("player: ", player_name)
                print("You win!")

        elif player_name == "P":
            if computer == "S":
                print("computer: ", computer)
                print("player: ", player_name)
                print("You lose!")
            if computer == "R":
                print("computer: ", computer)
                print("player: ", player_name)
                print("You win!")
        #else:
            #print("Inputted choice is in small caps")
game_start()

def game_replay():
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        game_start()
    elif play_again != "no":
            print("Bye!")
    else:
        game_replay()

game_start()
game_replay()

