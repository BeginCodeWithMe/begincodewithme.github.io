<!-- <h1> Rock, Paper and Scissor Game using Python </h1>
 -->
import random

while True:
   
<!--     Random choices for computer -->
    choices = ["rock", "paper", "scissor"]
    
    computer = random.choice(choices)
    
<!--    Take input from player -->
    player = input("Player Turn ( rock, paper, scissor ): ")
    
<!--    To show what thing the player and computer choose -->
    print("Player choose" + " " + player)
    print("computer choose" + " " + computer)
   
<!--     Condition for what to do when both ( player and computer ) chooses the same thing -->
    if player == computer:
        print("Game Tie")
    
<!--     Conditions for what to do when player and computer choose different thing -->
    elif player == "rock":
        if computer == "paper":
            print("Computer Win")
        else:
            print("Player Win")
    
    elif player == "paper":
        if computer == "rock":
            print("Player Win")
        else:
            print("Computer Win")
    
    elif player == "paper":
        if computer == "scissor":
            print("Computer Win")
        else:
            print("Player Win")
    
<!--     # What to do if player enter other than the available choices -->
    else:
        print("Invalid Input")
