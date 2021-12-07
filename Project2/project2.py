#This is the game for fun! And as we all have played this game in our teengae this is a game for teens,
#As most of the time nowadays they spend their time on electronics, so via phone they will be playing this stone,paper,scissors

import random
choices = ["Stone", "Paper", "Scissors"]
computer = random.choice(choices)
Gamer = False
Computer_score = 0
Gamer_score = 0
#Here user will be asked to choose from stone, paper, Scissors. So when they choose one computer will choose there thing to play
while True:
    Gamer = input("Stone, Paper or  Scissors?").capitalize()
    #Conditions of Stone,Paper and Scissors
    if Gamer == computer:
        print("That is a tie")
    elif Gamer == "Stone":
        if computer == "Paper":
            print("You lost this game", computer, "covers", Gamer)
            Computer_score+=1
        else:
            print("You won this game", Gamer, "smashes", computer)
            Gamer_score+=1
    elif Gamer == "Paper":
        if computer == "Scissors":
            print("You lost this game", computer, "cut", Gamer)
            Computer_score+=1
        else:
            print("You won this game", Gamer, "covers", computer)
            Gamer_score+=1
    elif Gamer == "Scissors":
        if computer == "Stone":
            print("You lost this game", computer, "smashes", Gamer)
            Computer_score+=1
        else:
            print("You won this game", Gamer, "cut", computer)
            Gamer_score+=1
#This is the end of the game if user wants to end the game and see the final scores
#Of how many times and you will get a final result of user and computer, so that you can 
#decide who won this game.
    elif Gamer=='End':
        print("Final Scores is:")
        print(f"Computer:{Computer_score}")
        print(f"Gamer:{Gamer_score}")
        break