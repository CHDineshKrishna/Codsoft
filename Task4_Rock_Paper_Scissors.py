"""
CODSOFT Python Programming Internship
Rock-Paper-Scissors Game

Rules:
- Rock beats scissors.
- Scissors beats paper.
- Paper beats rock.
"""

import random

CHOICES = ("rock", "paper", "scissors")


def determine_winner(user_choice, computer_choice):
    """Return 'tie', 'user', or 'computer' for a round."""
    if user_choice == computer_choice:
        return "tie"

    winning_combinations = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper",
    }

    if winning_combinations[user_choice] == computer_choice:
        return "user"
    return "computer"


def main():
    user_score = 0
    computer_score = 0
    ties = 0

    print("=" * 40)
    print("       ROCK - PAPER - SCISSORS")
    print("=" * 40)
    print("Rules: Rock beats scissors, scissors beats paper,")
    print("       paper beats rock.")
    print("Enter rock, paper, or scissors to play.")
    print("Enter q to quit.\n")

    while True:
        user_choice = input("Your choice: ").strip().lower()

        if user_choice in ("q", "quit", "exit"):
            break

        if user_choice not in CHOICES:
            print("Invalid choice. Please enter rock, paper, or scissors.\n")
            continue

        computer_choice = random.choice(CHOICES)
        winner = determine_winner(user_choice, computer_choice)

        print(f"\nYou chose:      {user_choice}")
        print(f"Computer chose: {computer_choice}")

        if winner == "tie":
            ties += 1
            print("Result: It's a tie!")
        elif winner == "user":
            user_score += 1
            print("Result: You win this round!")
        else:
            computer_score += 1
            print("Result: The computer wins this round.")

        print(f"Score — You: {user_score} | Computer: {computer_score} | Ties: {ties}")
        print("-" * 40)

        play_again = input("Would you like to play again? (y/n): ").strip().lower()
        if play_again not in ("y", "yes"):
            break
        print()

    print("\n========== FINAL SCORE ==========")
    print(f"You: {user_score} | Computer: {computer_score} | Ties: {ties}")
    if user_score > computer_score:
        print("Overall result: You won!")
    elif computer_score > user_score:
        print("Overall result: The computer won.")
    else:
        print("Overall result: It's a tie!")
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
