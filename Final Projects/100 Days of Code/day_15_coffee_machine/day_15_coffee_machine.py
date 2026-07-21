MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

PROFIT = 0


def turn_off():
    """Turns off the coffee machine."""
    print("Turning off the coffee machine. Goodbye!")
    exit()


def print_report():
    """Prints a report of the current resources."""
    print("Current resources:")
    for resource, amount in resources.items():
        print(f"{resource.capitalize()}: {amount}ml" if resource != "coffee" else f"{resource.capitalize()}: {amount}g")
    print(f"Money: ${PROFIT:.2f}")


def check_resources(drink):
    """Checks if there are enough resources to make the drink."""
    for ingredient, amount in MENU[drink]["ingredients"].items():
        if resources[ingredient] < amount:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Returns True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        global PROFIT
        PROFIT += drink_cost
        if change > 0:
            print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    

def make_coffee(drink):
    """Deducts the required ingredients from the resources and serves the coffee."""
    for ingredient, amount in MENU[drink]["ingredients"].items():
        resources[ingredient] -= amount
    print(f"Here is your {drink}. Enjoy! ☕")

is_on = True
while is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "off":
        turn_off()
    elif user_choice == "report":
        print_report()
    else:
        if user_choice in MENU:
            if check_resources(user_choice):
                payment = process_coins()
                if is_transaction_successful(payment, MENU[user_choice]["cost"]):
                    make_coffee(user_choice)
        else:
            print("Invalid selection. Please choose espresso, latte, or cappuccino.")