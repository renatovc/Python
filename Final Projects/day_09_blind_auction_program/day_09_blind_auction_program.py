import art

def find_highest_bid(users):
    winner = ""
    highest_bid = 0
    for key in users:
        bid_amount = users[key]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = key

    print(f"The winner is {winner} with a bid of ${highest_bid}.")

print(art.logo)
print("Welcome to the Secret Auction Program.")

users = {}
still_adding_user = True

while still_adding_user:
    user_name = input("What is your name?: ")
    user_bid = int(input("What is your bid?: $"))
    users[user_name] = user_bid

    still_playing = input("Are there any other bidders? Type 'yes' or 'no': ")
    print("\n" * 20)

    if still_playing == "no":
        still_adding_user = False
        find_highest_bid(users)