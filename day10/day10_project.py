# To create a Calculator with functions

import operation_function as calc
import os 
print("Welcome to Basic Calculator")

continue_again = True
while continue_again == True:
   
   result = calc.operation(int(input("What's the first Number: ")),
                           int(input("What's the second Number: ")),
                           input("Select an operation ('+', '-', '*', '/', '%'): "))
   
   print(result)
   
   try_again = input("Want to make another process (yes/no)? ")

   if try_again == "yes":
        os.system('cls')
   else:
       continue_again = False
