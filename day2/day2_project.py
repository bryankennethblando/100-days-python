# creating a tip calculator
print ("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip = (float(input("How much tip would you like to give? 10, 12, or 15? ")) / 100) * bill
total_tip = bill + tip
split_bill = int(input("How many people to split the bill? "))
total_bill = total_tip / split_bill
print (f"Each person should pay: ${round(total_bill, 2)}")