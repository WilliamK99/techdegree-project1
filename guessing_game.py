"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
Author - William Kubicz
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    #TODO Exceeption Handling
    #TODO 
    high_score = []
    name = input("Welcome to the Number Guessing Game, What is your name?  ") 
    again = "yes"

    while again == "yes":
        answer = random.randrange(1,11)
        count = 1
        while True:
            try:
                guess = int(input("Hello {} pick a number between 1 and 10 ".format(name)))
            except ValueError:
                print("Please enter a valid number")
                continue
            if guess < 1 or guess > 10:
                print("Number must be between 1 and 10")
                continue
            if guess == answer:
                print("Got it!, the number was {}".format(answer))
                break
            elif guess < answer:
                print("It' higher!")
                count += 1
                continue
            elif guess > answer:
                print("It's lower")
                count += 1
                continue
        print("Great job {}, It took you {} tries!".format(name,count))
        again = input("Would you like to play again?  Yes/No ").lower()
        #if again.lower() == "yes":
        #    continue
        #elif again.lower() == "no":
        #    break
        #else:
        #    print(("Assuming you meant Yes with yoour response"))
    print("Thanks for playing {}! Have a good day!".format(name))  


# Kick off the program by calling the start_game function.
start_game()
