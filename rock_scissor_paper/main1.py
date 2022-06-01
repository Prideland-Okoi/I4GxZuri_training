from random import choice

#create a list of play options
list = ["R", "P", "S"]

while True:
    computer = choice(list)

    player = input("Please select your choice: R for Rock, P for Paper, S for Scissors?")

    if player == computer:
        print("Tie!")
    elif player == "R":
        if computer == "P":
            print("You lose!", "Player's choice: Rock. Computer's choice: Paper", computer, "covers", player)
        else:
            print("You win!", "Player's choice: Rock. Computer's choice: Stone", player, "smashes", computer)
        break
    elif player == "P":
        if computer == "S":
            print("You lose!", "Player's choice: Paper. Computer's choice: Stone", computer, "cut", player)
        else:
            print("You win!", "Player's choice: Paper. Computer's choice: Rock", player, "covers", computer)
        break
    elif player == "S":
        if computer == "R":
            print("You lose...", "Player's choice: Stone. Computer's choice: Rock", computer, "smashes", player)
        else:
            print("You win!","Player's choice: Stone. Computer's choice: Paper", player, "cut", computer)
        break
    else:
        print("That's not a valid play. Enter choice in capital letter!")

