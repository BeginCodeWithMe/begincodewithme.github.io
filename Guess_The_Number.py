# Guess The Number By User :

import random
x = ""
user = ""
quit = 0
while user != quit:
    x = int(input(" Enter limit of the Number till you want to Guess: "))
    computer = random.randint(1, x)
    user = ""
    print("\n")
    while user != computer:
        user = int(input("If you want to Quit the Game Type 0 else "
                         "\n Guess the Number: "))
        if user == quit:
            print("Quiting...")
            break
        elif user > computer:
            print("Ohh! too High")
        elif user < computer:
            print("Ohh! too Low")
        elif user == computer:
            print("Boom! you Guess the Right Number")
        else:
            print(
                "Ohh please check your Number it's out of the Limit You have Entered Above")
