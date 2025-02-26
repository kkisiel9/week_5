import random

def player_choice(player):
    """
    Defines the process to get to player choice
    :return: str of whatever the user enters
    We use an if statement to determine if the user value entry is in one of the option
    """
    choice = input("Enter R for Rock, P for Paper, or S for Scissors: ")
    if choice in ['R', 'P', 'S']:
        return choice
    return player_choice(player)

def computer_choices():
    computer_choice_dict = {"1":"R", "2":"P", "3":"S"}
    random_choice = str(random.randint(1,3))
    return computer_choice_dict[random_choice]

def winner(player1, computer):
    """

    :param player1: First player would need to enter from the choice of the set - R,P,S
    :param computer: Second player would need to enter from the choice of the set - R, P,S
    :return: A string of the winner
    """
    if player1 == computer:
        return "It's a tie!"
    elif (player1 == 'R' and computer == 'S') or \
         (player1 == 'P' and computer == 'R') or \
         (player1 == 'S' and computer == 'P'):
        return "Player 1 - You win!"
    else:
        return "Player 2 - You win!"


def main():
    """
    Runs the game and prints the results.
    """
    player1_input = player_choice("Player 1")
    print(f"Player 1 chose: {player1_input}")
    computer_input = computer_choices()
    print(f"Computer chose: {computer_input}")
    win = winner(player1_input, computer_input)
    print(win)


# test the function
# Test player_choice() independently
# i do not want this main function to be called when this file is imported (a.k.a. a module) into another file
if __name__ == "__main__":
    main()



