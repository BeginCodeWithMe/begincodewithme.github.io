<h1> Rock, Paper and Scissor Game using Python </h1>

import random

While True:
   
<!--    Random choices for computer -->
    choice  = ["rock", "paper", "scissor"]
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
        
  <br>      
  <hr>
  <br>
  <h1> Gusee The Number Game </h1>
  
  # Guess The Number By User :

import random

x = ""
user = ""
quit = 0
while user != quit:

   # To take user input 
    x = int(input(" Enter limit of the Number till you want to Guess: "))
   
   # Computer Choose a random number between the range 1 to x
    computer = random.randint(1, x)
    user = ""
    print("\n")
    while user != computer:
        user = int(input("If you want to Quit the Game Type 0 else "
                         "\n Guess the Number: "))
        if user == quit:
            print("Quiting...")
            break
      
   # If user guess a number higher than the number choosed by the computer
      
        elif user > computer:
            print("Ohh! too High")
            
   # If user guess a number lower than the number choosed by the computer
   
        elif user < computer:
            print("Ohh! too Low")
            
  # If user guess the right number
        elif user == computer:
            print("Boom! you Guess the Right Number")
            
  # If user guess a number higher than the range
        else:
            print(
                "Ohh please check your Number it's out of the Limit You have Entered Above")
