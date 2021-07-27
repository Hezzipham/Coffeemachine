# Coffee Machine
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
profit = 0

def is_resource_sufficient(order_ingredients):
    """Check if ingredient is enough"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True
def process_coins():
    """Return total coin inserted"""
    print("please insert coin")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Check if the payment is accepted, out put is True/ False"""
    if money_received > drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is {change} in change")
        global profit
        profit += drink_cost
        return True
    elif money_received == drink_cost:
        print(f"Received ${money_received}")
        return True
    else:
        print(f"Sorry that's not enough money. {money_received} refunded.")
        return False
def make_coffee(drink_name, drink_ingredients):
    """Deduct the ingredients from the resources"""
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"Here is our {drink_name} ☕️")

is_on = True

while is_on:
    choice = input("What do you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water {resources['water']}ml")
        print(f"Milk {resources['milk']}ml")
        print(f"Coffee {resources['coffee']}g")
        print(f"Money {profit}")
    else:
        drink = MENU[choice]
        print(f"{choice} price is {drink['cost']}$")
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(choice, drink["ingredients"])




