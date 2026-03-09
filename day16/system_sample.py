from coffee_system import machine_resources as system_resource
from coffee_system import preperation as prep
from coffee_system import money 
import subprocess
system_on = True
while system_on:

    valid_drinks = ['expresso', 'latte', 'cappuccino', 'americano', 'mocha', 'macchiato']
    check_order = ""

    while check_order == 'inpect' or check_order == 'add' or check_order not in valid_drinks:

        customer_input = input("What would you like (expresso, latte, cappucino, americano, mocha, macchiato)? ").lower()
        check_order = customer_input

        if customer_input == "inspect":
            system_resource.inspect()

        elif customer_input == "refill":
           system_resource.inspect()
           system_resource.refill('Enter the amount to refill: ')
        
        elif customer_input == "upgrade":
            system_resource.upgrade(to_upgrade=True)

        elif customer_input not in valid_drinks:
            print("sorry you've entered the wrong order")

    customer_payment = money.coins()
    is_payment_enough, message = money.money_checked(customer_payment, customer_input)
    coffee_to_served = prep.make_a_coffee(customer_input)

    if is_payment_enough:
        print(message)
        print(coffee_to_served)
    else:
        print(message)
    
    another_customer = prep.process_again('Process order (y/n): ')

    if not another_customer:
        system_on = False
    else:
        subprocess.run('cls', shell=True)