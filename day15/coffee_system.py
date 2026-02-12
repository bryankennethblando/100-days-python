# Coffee Machine System

Menu = {
    'expresso' : {
        'ingredients': {
            'water' : 50,
            'coffee' : 18
        },
        'cost' : 1.5
    },

    'latte' : {
        'ingredients' : {
            'water' : 200,
            'milk' : 150,
            'coffes' : 24
        },
        'cost' : 2.5
    },

    'cappucino' : {
        'ingredients' : {
            'water' : 250,
            'milk' : 100,
            'coffee' : 24
        },
        'cost' : 3.0
    }

}

resources = {
    'water' : 300,
    'milk' : 200,
    'coffee' : 100
}

profit = 0

def coins():
    
    print("Insert coins here: ")
    quarters = int(input("How many quarter? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    total_inserted_coins = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    print(f" We received ${total_inserted_coins}")

    return total_inserted_coins

def refill(which_resources, how_many):

    for resource in resources:
        if resource == which_resources:
            resources[resource] += how_many
            break
        else:
            resources[resource] += how_many

    return resources


def money_checked(total_received_coins, drink_name):
    global profit
    cost = Menu[drink_name]['cost']
    
    if total_received_coins < cost:
        return False, "Sorry that's not enough money. Money refunded."
    else:
        change = round(total_received_coins - cost, 2)
        if change > 0:
            profit += cost
            return True, f"Here is your ${change} change."
        
        profit += cost
        return True, "you've the exact amount, thank you"


def make_a_coffee(drink_name):

    ingredients = Menu[drink_name]['ingredients']

    for item in ingredients:
        if resources[item] < ingredients[item]:
            return "can't make the coffee, not enough ingredients, please ask the personel to refill the machine"
        else:
            resources[item] -= ingredients[item]

    return f"here's your drink {drink_name}"

def inspect_resources():

    for key, amount in resources.items():
        if key == "coffee":
            print(f"{key} : {amount}kg")
            break

        print(f"{key} : {amount}ml")

    print(f"Money : ${profit}")

def process_again(customer_input):
    if customer_input == 'y':
        return True
    else:
        return False