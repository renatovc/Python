import game_data
import art
import random

print(art.logo)

"""Compare A: [Name], a [Description], from [Country].
    - vs logo -
   Against B: [Name], a [Description], from [Country].
"""

def choose_random_account():
    """Randomly chooses from the game data."""
    choose_a = random.choice(game_data.data)
    choose_b = random.choice(game_data.data)

    if choose_a == choose_b:
        choose_b = random.choice(game_data.data)

    return choose_a, choose_b


def higher_or_lower():
    """Main function to run the game."""
    score = 0
    game_should_continue = True
    account_a, account_b = choose_random_account()

    while game_should_continue:
        print(f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}.")
        print(art.vs)
        print(f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}.\n")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        print("\n" * 20)
        print(art.logo)

        a_follower_count = account_a['follower_count']
        b_follower_count = account_b['follower_count']

        is_correct = (guess == 'a' and a_follower_count > b_follower_count) or (guess == 'b' and b_follower_count > a_follower_count)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.\n")
            account_a = account_b
            account_b = random.choice(game_data.data)
            while account_a == account_b:
                account_b = random.choice(game_data.data)
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}.")

higher_or_lower()