import random

def prompt_user_choice():
    """Prompt the user to choose rock, paper, or scissors."""
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        user_choice = input("Choose rock, paper, or scissors: ").lower()
    return user_choice

def generate_computer_choice():
    """Generate a random choice (rock, paper, or scissors) for the computer."""
    return random.choice(["rock", "paper", "scissors"])

def determine_round_winner(user_choice, computer_choice):
    """Determine the winner based on the user's choice and the computer's choice."""
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def main():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock-Paper-Scissors!")

    while True:
        user_choice = prompt_user_choice()
        computer_choice = generate_computer_choice()

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_round_winner(user_choice, computer_choice)

        if result == "user":
            user_score += 1
            print("You win!")
        elif result == "computer":
            computer_score += 1
            print("Computer wins!")
        else:
            print("It's a tie!")

        print(f"Score - You: {user_score}, Computer: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
