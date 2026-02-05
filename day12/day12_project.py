# Guessing the number game
import random as r
import os 

def modes(option):
    if option == "e":
        guess_count = 10
        return f"You only have {guess_count} try's to guess the number", guess_count
    elif option == "h":
        guess_count = 5
        return f"You only have {guess_count} try's to guess the number", guess_count

def condition(num, computer_num, tries):
    if num == computer_num:
        return f"Congratulations you win!", f"You guessed it with {tries} tries left"
    
    tries -= 1

    if num < computer_num:
        hint = "No, Higher"
        
    elif num - computer_num <= 5:
        hint =  "No, Closer"
    else:
        hint = "No, Lower"

    return hint, f"You have {tries} tries left"
    
    
    
computer_number = r.randint(1, 100)
print("Welcome to Guess the Number Challenge")

continue_again = True
while continue_again == True:
    selection = input("Type 'e' for easy mode and 'h' for hard mode: ")
    text, guess_times = modes(selection)
    print(computer_number)
    print(text)
    while guess_times > 0:
        user_guess = int(input("Guess: "))
        
        who_win, tries_left = condition(user_guess, computer_number, guess_times)
        print(who_win)
        print(tries_left)
        if "Congratulations" in who_win:
            break
        elif guess_times == 0:
            print("Sorry you lose!")
            print(f"the number you failed to guess {computer_number}")
        else:
            guess_times -= 1
       

    try_again = input("Type 'y' to try again and 'n' to exit the game: ").lower()

    if try_again == "y":
        os.system('cls')
        print("Welcome to Guess the Number Challenge")
    else:
        continue_again = False