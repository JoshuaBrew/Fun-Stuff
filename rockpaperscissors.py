import random

choices = ["rock", "paper", "scissors"]

computer = random.choices(choices)[0]
                                   
player = None

while player not in choices:
    player = input("rock, paper, or scissors?: ")
    player = player.strip().lower()


if player == computer:
    print ("computer: ", computer)
    print("player: ", player)
    print ("Tie!")
elif player == "rock":
    if computer == "paper":
        print ("computer: ", computer)
        print("player: ", player)
        print ("Take the L!")
    if computer == "scissors":
        print ("computer: ", computer)
        print ("player: ", player)
        print ("Dub City!")
elif player == "scissors":
    if computer == "rock":
        print ("computer: ", computer)
        print("player: ", player)
        print ("Take the L!")
    if computer == "paper":
        print ("computer: ", computer)
        print ("player: ", player)
        print ("Dub City!")
elif player == "paper":
    if computer == "scissors":
        print ("computer: ", computer)
        print("player: ", player)
        print ("Take the L!")
    if computer == "rock":
        print ("computer: ", computer)
        print ("player: ", player)
        print ("Dub City!")
else:
    print("Hi")
