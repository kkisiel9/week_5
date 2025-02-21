# Prompt user input
print("Welcome to the Rock, Paper, Scissors game.")
# create a loop for the game to be able to run multiple times
while True:
    human_choice = input("Chose R, P or S:")
    # create a variable to store the human's choice
    if human_choice == "R":
        human_choice = "Rock"
    elif human_choice == "P":
        human_choice = "Paper"
    else:
        human_choice = "Scissors"
    # create a codnition and convert the single letter string into a full answer
    # generate random value
    import random
    comp_choice = random.randrange(0,2)
    # generate random in from the tange above through importing the ranfom module
    # conversion of the computer choice/random integer into a string which corresponds to r/p/s
    if  comp_choice == 0:
        comp_choice = "Rock"
    elif comp_choice == 1:
        comp_choice = "Paper"
    else:
        comp_choice = "Scissors"
    print(f"You chose {human_choice} and the computer chose {comp_choice}")
    print("Hence...")
    # interact with the user through string formatting to let them know computer choice
    def result(comp_choice, human_choice):
        """
        This function defines the result of the game through comparing the computer and human choice
        :param comp_choice: random int chosen by the computer from 0-2 range
        :param human_choice: input- R, P, S

        """
        if human_choice == comp_choice:
            print("It's a tie!")
        elif (human_choice == "rock" and comp_choice == "scissors") or \
             (human_choice == "scissors" and comp_choice == "paper") or \
             (human_choice == "paper" and comp_choice == "rock"):
           print("You win!")
        else:
           print("You lose!")
    # function defined above - could this be done not using print?
    result(comp_choice, human_choice)
    # call function
    question = input("Want to play again? Y/N")
    if question == "No":
        break
   #give user the option to play again