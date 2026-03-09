
Menu = {
    'espresso' : {
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
            'coffee' : 24
        },
        'cost' : 2.5
    },

    'cappuccino' : {
        'ingredients' : {
            'water' : 250,
            'milk' : 100,
            'coffee' : 24
        },
        'cost' : 3.0
    },

    'americano' : {
        'ingredients' : {
            'water' : 250,
            'coffee' : 18
        },
        'cost' : 2.0
    },

    'mocha' : {
        'ingredients' : {
            'water' : 50,
            'milk' : 150,
            'coffee' : 24,
            'chocolate' : 30
        },
        'cost' : 3.5
    },

    'macchiato' : {
        'ingredients' : {
            'water' : 50,
            'milk' : 20,
            'coffee' : 18
        },
        'cost' : 2.8
    }
}

resources = {
    'water' : 300,
    'milk' : 200,
    'coffee' : 100,
    'chocolate' : 200
}

profit = {
    'money' : 0
}

class machine_resources:
    # triggers whent the ml to refill is over the capacity limit
    def capacity_limit(self, ingredient, to_refill):
        if to_refill > resources[ingredient]:
            print("sorry you've reach the capacity limit of this resource container")
            print("upgrade the container first before refilling this amount")
            return False
        return True
        
        
    # to check if the operator wants to upgrade the resources limit
    def upgrade(self, to_upgrade=False):
        if to_upgrade:
            resource = input('which resources?')
            container_size = input(int(f'size of the container to be added on the {resource}'))
            resources[resource] = container_size
        return resources

    # the operator can refill specific resources and even all of it
    def refill(self, how_many):
        for ingredient in resources:
            if self.capacity_limit(ingredient, how_many):
                resources[ingredient] += how_many
        return resources
    
    # for inspecting the resources of the machine
    def inspect():
        for key, amount in resources.items():
            if key == "coffee":
                print(f"{key} : {amount}kg")
                break
            print(f"{key} : {amount}ml")
        print(f"Money : ${profit}")


class money:
    # to collect the coins the customer placed into the machine
    def coins():
        
        print("Insert coins here: ")
        quarters = int(input("How many quarter? "))
        dimes = int(input("How many dimes? "))
        nickels = int(input("How many nickels? "))
        pennies = int(input("How many pennies? "))
        total_inserted_coins = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
        print(f" We received ${total_inserted_coins}")

        return total_inserted_coins

    # checking if the money recieved was sufficient for the order
    def money_checked(total_received_coins, drink_name):
        cost = Menu[drink_name]['cost']
        
        if total_received_coins < cost:
            return False, "Sorry that's not enough money. Money refunded."
        else:
            change = round(total_received_coins - cost, 2)
            if change > 0:
                profit['money'] = cost
                return True, f"Here is your ${change} change."
            
            profit['money'] = cost
            return True, "you've the exact amount, thank you"

class preperation:

    def make_a_coffee(drink_name):

        ingredients = Menu[drink_name]['ingredients']

        for item in ingredients:
            if resources[item] < ingredients[item]:
                return "can't make the coffee, not enough ingredients, please ask the personel to refill the machine"
            else:
                resources[item] -= ingredients[item]

        return f"here's your drink {drink_name}"

    def process_again(customer_input):
        if customer_input == 'y':
            return True
        else:
            return False