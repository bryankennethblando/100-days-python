import coffee_system as coffee
import os

another_process = True
while another_process == True:

    valid_drinks = ['expresso', 'latte', 'cappuccino']
    check_order = ""

    while check_order == 'inpect' or check_order == 'add' or check_order not in valid_drinks:

        customer_order = input("What would you like (expresso, latte, cappucino)? ").lower()
        check_order = customer_order

        if customer_order == "inspect":
            coffee.inspect_resources()

        elif customer_order == "refill":
            coffee.inspect_resources()
            refilling = coffee.refill(input("Which ingredient do you want to refill? "), int(input("How many? ")))

        elif customer_order not in valid_drinks:
            print("sorry you've entered the wrong order")

    customer_payment = coffee.coins()
    is_payment_enough, message = coffee.money_checked(customer_payment, customer_order)
    coffee_to_served = coffee.make_a_coffee(customer_order)

    if is_payment_enough == False:
        print(message)
    else:
        print(message)
        print(coffee_to_served)
    
    is_there_customer = coffee.process_again(input("Want to order again (y/n)? ").lower)

    if is_there_customer == True:
        os.system('cls')
    else:
        continue_again = False