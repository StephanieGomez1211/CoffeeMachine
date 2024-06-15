import art
# from menu import resources,MENU, secretwords, coins
from menu import *

print(art.logo)
profit: float = 0.0
not_off: bool = True
current_resources: dict = resources

def get_key(order_resources: list[str]) -> list[str]:
    return [key for key,value in order_resources.items()]


def get_cost(ur_order: str) -> float:
    return MENU[ur_order]["cost"]


def get_ingredients(ur_order: str, ingredient: str) -> int:
    return MENU[ur_order]["ingredients"][ingredient]


def check(ur_order: str, ingredients: str) -> bool:
    return MENU[ur_order]["ingredients"][ingredients] <= current_resources[ingredients]


def make_coffee(ur_order: str) -> None:
    for ingredient in get_key(MENU[ur_order]['ingredients']):
        current_resources[ingredient] -= get_ingredients(ur_order,ingredient)



def is_in_menu(menu: str) -> bool:
    return menu in MENU


def insert_coins(coin: str) -> float:
    # return float(input(f"How many {coin}?: "))
    user_input = None
    while user_input is None:
        try:
            user_input = float(input(f"How many {coin}?: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    return user_input


def process_coins(ur_order: str, payment: float) -> float:
    if is_payment_enough(ur_order,payment):
        return payment - get_cost(ur_order)
    else:
        return payment


def is_payment_enough(ur_order: str,payment: float) -> bool:
    return payment >=get_cost(ur_order)


def profits(ur_order: str, payment: float) -> None:
    global profit
    profit += payment
    profit -= process_coins(ur_order, payment)
    # print(f" Profit: {profit}")


def order(ur_order: str) -> None:
    global not_off
    enough_resources: bool = True
    #Check for resources
    for ingredient in get_key(MENU[ur_order]['ingredients']):
        if check(ur_order,ingredient):
            ...
            # print(f"Enough {ingredient}")
        else:
            print(f"Sorry there is not enough {ingredient}.")
            enough_resources = False
    #
    #Process Coin
    if enough_resources:
        print(f"Please insert coins.")
        payment: float = 0.0
        for key, value in coins.items():
            payment += float((insert_coins(key)) * float(coins[key]))
        print(f"Here is ${process_coins(ur_order,payment):.2f} change.")
        if is_payment_enough(ur_order,payment):
            make_coffee(ur_order)
            print(f"Here is your {ur_order} ☕ enjoy!")
        else:
            print(f"Sorry that's not enough money. Money Refunded.")
        profits(ur_order,payment)
    #

def execute_secretword(secretword: str) -> None:
    global not_off
    if secretword == "report":
        print(f"Water: {current_resources['water']}ml")
        print(f"Milk: {current_resources['milk']}ml")
        print(f"Coffee: {current_resources['coffee']}g")
        print(f"Money: ${profit:.2f}")
    if secretword == "off":
        print("Turning Off Machine. . .")
        not_off = False

def main():
    while not_off:
        your_order: str = input("What would you like? (espresso/latte/capuccino): ").lower()
        if is_in_menu(your_order):
            order(your_order)
        elif your_order in secretwords:
            execute_secretword(your_order)
        else:
            print("Invalid order. Order Again.")

if __name__ == '__main__':
    main()