import random
# Prompt user input

def result(comp_choice, human_choice):
    """
    This function defines the result of the game through comparing the computer and human choice
    :param comp_choice: random int chosen by the computer from 0-2 range
    :param human_choice: input- R, P, S
    """
    if human_choice == comp_choice:
        return "tie"
    elif (human_choice == "rock" and comp_choice == "scissors") or \
            (human_choice == "scissors" and comp_choice == "paper") or \
            (human_choice == "paper" and comp_choice == "rock"):
        return "win"
    else:
        return "lose"

print("Welcome to the Rock, Paper, Scissors game.")
# create a loop for the game to be able to run multiple times
while True:
    while True:
        human_choice = input("Chose R, P or S:")
    # create a variable to store the human's choice, break the loop and move on if condition met
        if human_choice == "R":
            human_choice = "Rock"
            break
        elif human_choice == "P":
            human_choice = "Paper"
            break
        elif human_choice == "S":
            human_choice = "Scissors"
            break
        else:
            print("Invalid input, try again")

    #     loop if input not one of the three options
    # create a codnition and convert the single letter string into a full answer
    # generate random value

    comp_choice = random.randrange(0,2)
    # generate random in from the tange above through importing the ranfom module
    # conversion of the computer choice/random integer into a string which corresponds to r/p/s
    if  comp_choice == 0:
        comp_choice = "Rock"
    elif comp_choice == 1:
        comp_choice = "Paper"
    else:
        comp_choice = "Scissors"
    # interact with the user through string formatting to let them know computer choice
    print(f"You chose {human_choice} and the computer chose {comp_choice}")
    print("Hence...")

    #call function and give options which are contrasted against returned result
    r = result(comp_choice, human_choice)
    if r == "tie":
            print("It's a tie!")
    elif r == "win":
            print("Wooo, you win!")
    else:
            print ("Sorry, you lose...")


    question = input("Want to play again? Y/N")
    if question == "N":
        break
   #give user the option to play again or leave