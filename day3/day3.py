# # Coditionals and modulo
# number = int(input("Enter your number: "))
# if number % 2 == 0:
#     print ("this number is an EVEN number")
# else:
#     print ("this number is an ODD number")

# nested if statements
print ("Welcome to python pizza delivery")
size = input("What size of pizza do you want? S, M, or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_chesse = input("Do you want extra cheese? Y or N: ")

# price of their pizza based on the size
price = 0

if size == "S":
    price += 15

    # adding extra 2 based on the pepperoni choice
    if pepperoni == "Y":
        price += 2

elif size == "M":
    price += 20

    if pepperoni == "Y":
        price += 3
        
elif size == "L":
    price += 25
    
    if pepperoni == "Y":
        price += 3
        
else:
    print ("order is out of bounds")

# adding extra 2 based if they want cheese

if extra_chesse == "Y":
    price += 1

print (f"The total price of the pizza is: ${price}")