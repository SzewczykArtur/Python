'''
Simulation how coffee machine work.
'''

import menu

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0


def user_choice(drink):
    coffee = []
    for i in drink.keys():
        coffee.append(i)
    seperator = '/'
    coffee_menu = seperator.join(coffee)
    choice = input(f'What would you like?({coffee_menu}): ')
    return choice


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True


def insert_money():
    print('Please insert coin: ')
    quarter = int(input('How many quarters: '))
    dime = int(input('How many dimes: '))
    nickle = int(input('How many nickles: '))
    pennie = int(input('How many pennies: '))
    return (0.25 * quarter) + (0.10 * dime) + (0.05 * nickle) + (0.01 * pennie)


def print_report(resource, money):
    """Returns report about resource and money"""
    for k,v in resource.items():
        print(k.capitalize() + ': ' + str(v))
    print(f'Money: ${money}')


def payment_check(coffee_cost):
    user_input_money = insert_money()
    if coffee_cost > user_input_money:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = user_input_money - coffee_cost
        print(f'Here is your coffee and change ${change}')
        return coffee_cost


def upgrade_container(resource, coffee_ingredient):
    resource['milk'] -= coffee_ingredient['milk']
    resource['water'] -= coffee_ingredient['water']
    resource['coffee'] -= coffee_ingredient['coffee']
    return resource


is_on = True
while is_on:
    user_input = user_choice(menu.MENU)
    if user_input.lower() == 'off':
        is_on = False
        print('Machine is turn off!')
    elif user_input.lower() == 'latte':
        latte_cost = menu.MENU['latte']['cost']
        profit += payment_check(latte_cost)
        upgrade_container(resources,menu.MENU['latte']['ingredients'])
    elif user_input.lower() == 'espresso':
        espresso_cost = menu.MENU['latte']['cost']
        profit += payment_check(espresso_cost)
    elif user_input.lower() == 'cappuccino':
        cappuccino_cost = menu.MENU['cappuccino']['cost']
        profit += payment_check(cappuccino_cost)
    elif user_input.lower() == 'report':
        print_report(resources, profit)
    else:
        print('Wrong choose')