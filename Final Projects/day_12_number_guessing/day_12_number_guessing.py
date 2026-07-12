import art

def guessing_game(difficulty):
    import random

    number_to_guess = random.randint(1, 100)
    attempts = 10 if difficulty == "easy" else 5

    print(f"You have {attempts} attempts remaining to guess the number.")

    while attempts > 0:
        guess = int(input("Make a guess: "))

        if guess < number_to_guess:
            print("Too low.")
        elif guess > number_to_guess:
            print("Too high.")
        else:
            print(f"You got it! The answer was {number_to_guess}.")
            return

        attempts -= 1
        if attempts > 0:
            print(f"You have {attempts} attempts remaining to guess the number.")
        else:
            print(f"You've run out of guesses. The number was {number_to_guess}.")


print(art.logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

guessing_game(difficulty)