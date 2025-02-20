# This is a sample Python script.
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

def winner(player1, player2):
    """

    :param player1: First player would need to enter from the choice of the set - R,P,S
    :param player2: Second player would need to enter from the choice of the set - R, P,S
    :return: A string of the winner
    """
    if player1 == player2:
        return "It's a tie!"
    elif (player1 == 'R' and player2 == 'S') or \
         (player1 == 'P' and player2 == 'R') or \
         (player1 == 'S' and player2 == 'P'):
        return "Player 1 - You win!"
    else:
        return "Player 2 - You win!"


def main():
    """
    We are testing each functions
    :return:A print statement of each function
    """
    player1_input = player_choice("Player 1")
    print(f"Player 1 chose: {player1_input}")
    player2_input = player_choice("Player 2")
    print(f"Player 2 chose: {player2_input}")
    win = winner(player1_input, player2_input)
    print(win)


# test the function
# Test player_choice() independently
# i do not want this main function to be called when this file is imported (a.k.a. a module) into another file
if __name__ == "__main__":
    main()



