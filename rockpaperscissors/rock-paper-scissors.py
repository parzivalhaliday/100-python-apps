import random

def play_game(nickname):
    # Ask the user for their choice (rock, paper, or scissors)
    user_choice = input("Enter your choice (rock/paper/scissors): ")
    
    # Generate a random choice for the computer
    computer_choice = random.choice(["rock", "paper", "scissors"])
    
    # Print the user and computer's choices
    print(f"{nickname} chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Determine the winner of the game
    if user_choice == computer_choice:
        print("It's a tie!")
        return 'tie'
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print(f"{nickname} wins!")
            return 'user'
        else:
            print("Computer wins!")
            return 'computer'
    elif user_choice == "paper":
        if computer_choice == "rock":
            print(f"{nickname} wins!")
            return 'user'
        else:
            print("Computer wins!")
            return 'computer'
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print(f"{nickname} wins!")
            return 'user'
        else:
            print("Computer wins!")
            return 'computer'
    else:
        # Handle invalid user input
        print("Invalid input! You have not entered rock, paper or scissors, try again.")

# Ask the user for their nickname
nickname = input("Enter your nickname: ")

# Initialize scores to zero
user_score = 0
computer_score = 0

# Start the game loop
while True:
    # Play one round of the game
    winner = play_game(nickname)
    
    # Update the scores based on the winner of the round
    if winner == 'user':
        user_score += 1
    elif winner == 'computer':
        computer_score += 1
    
    # Print the current score
    print(f"Score: {nickname} {user_score} - Computer {computer_score}")
    
    # Ask the user if they want to play again
    play_again = input("Do you want to play again? (yes/no): ")
    
    # If the user does not want to play again, end the game loop
    if play_again.lower() != "yes":
        break

# Determine the winner of the game and print the final score
if user_score == computer_score:
    print("It's a tie!")
elif user_score > computer_score:
    print(f"{nickname} {user_score} - Computer {computer_score}: {nickname} wins!")
else:
    print(f"{nickname} {user_score} - Computer {computer_score}: Computer wins!")

# Print a message to thank the user for playing
print("Thanks for playing!")
