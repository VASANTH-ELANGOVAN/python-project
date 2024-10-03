import random

def number_guessing_game():
    num = random.randint(1, 100)
    score = 0
    print("WELCOME TO THE NUMBER GUESSING GAME!")
    print()
    difficulty_level = input("Enter the level of difficulty...Type 'easy' or 'hard': ").lower()

    if difficulty_level == "easy":
        attempts = 10
        print(f"You have {attempts} attempts to guess the number!")
    elif difficulty_level == "hard":
        attempts = 5
        print(f"You have {attempts} attempts to guess the number!")
    else:
        print("Invalid input! Exiting game...")
        return

    while attempts > 0:
        guess = int(input("Make a guess: "))
        
        if guess < num:
            print("Your guess is too low!")
            if num - guess <= 10:
                print("Hint: You're very close!")
        elif guess > num:
            print("Your guess is too high!")
            if guess - num <= 10:
                print("Hint: You're very close!")
        else:
            score += attempts * 10  # Bonus points for winning early
            print(f"Great! Your guess is correct...You won with a score of {score}!")
            break

        attempts -= 1
        print(f"You have {attempts} attempts left")

        if attempts == 0:
            print("You lost! Better luck next time.")
            print(f"The correct number was {num}")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        number_guessing_game()


number_guessing_game()
