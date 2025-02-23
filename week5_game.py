# random module to allow the computer to generate random choices
import random

# convert user input (R, P, S) to full names (Rock, Paper, Scissors)
def full_name(choice):
    """
    This function takes a letter input ('R', 'P', or 'S') and
    returns the full name of the choice (Rock, Paper, or Scissors).
    """
    if choice == 'R':
        return 'Rock'
    elif choice == 'P':
        return 'Paper'
    elif choice == 'S':
        return 'Scissors'
    else:
        return None  # returns None if the input is invalid

# function to determine the winner
def determine_winner(player_selection, computer_choice):
    """
    This function compares the user's choice and the computer's choice
    and determines the winner based on the game rules.
    """
    if player_selection == computer_choice:
        return "It's a draw!"  # both choices are the same

    # Winning conditions for the user
    elif (player_selection == 'Rock' and computer_choice == 'Scissors') or \
         (player_selection == 'Paper' and computer_choice == 'Rock') or \
         (player_selection == 'Scissors' and computer_choice == 'Paper'):
        return "You win!"  # player wins

    else:
        return "You lose!"  # Otherwise, the computer wins

# Main function to play the game
def play_game():
    """
    This function runs the Rock, Paper, Scissors game.
    It asks for user input, generates a computer choice, and displays the result.
    """
    # Prompt user for input (R, P, or S)
    user_input = input("Enter R for Rock, P for Paper, or S for Scissors: ").upper()

    # Convert user input to full name
    player_selection = full_name(user_input)

    # Check if user input is valid
    if player_selection is None:
        return "Invalid choice! Please enter R, P, or S."
        # Exits the function if input is invalid

    # Generate a random choice for the computer (0, 1, or 2)
    computer_random_choice = random.randint(0, 2)

    # Convert random number to Rock, Paper, or Scissors
    choices = ['Rock', 'Paper', 'Scissors']  # List representing choices
    computer_choice = choices[computer_random_choice]  # Pick choice from list

    # Display user and computer choices
    print(f"\nYou chose: {player_selection}")
    print(f"Computer chose: {computer_choice}")

    # Determine and display the winner
    result = determine_winner(player_selection, computer_choice)
    print(result)

# Run the game
play_game()



























#
# # This is a sample Python script.
# def player_choice(player):
#     """
#     Defines the process to get to player choice
#     :return: str of whatever the user enters
#     We use an if statement to determine if the user value entry is in one of the option
#     """
#     choice = input("Enter R for Rock, P for Paper, or S for Scissors: ")
#     if choice in ['R', 'P', 'S']:
#         return choice
#     return player_choice(player)
#
# def winner(player1, player2):
#     """
#
#     :param player1: First player would need to enter from the choice of the set - R,P,S
#     :param player2: Second player would need to enter from the choice of the set - R, P,S
#     :return: A string of the winner
#     """
#     if player1 == player2:
#         return "It's a tie!"
#     elif (player1 == 'R' and player2 == 'S') or \
#          (player1 == 'P' and player2 == 'R') or \
#          (player1 == 'S' and player2 == 'P'):
#         return "Player 1 - You win!"
#     else:
#         return "Player 2 - You win!"
#
#
# def main():
#     """
#     We are testing each functions
#     :return:A print statement of each function
#     """
#     player1_input = player_choice("Player 1")
#     print(f"Player 1 chose: {player1_input}")
#     player2_input = player_choice("Player 2")
#     print(f"Player 2 chose: {player2_input}")
#     win = winner(player1_input, player2_input)
#     print(win)
#
#
# # test the function
# # Test player_choice() independently
# # i do not want this main function to be called when this file is imported (a.k.a. a module) into another file
# if __name__ == "__main__":
#     main()



