# project hangman
import random as r
import hangman

list_of_words = ["dog", "cat", "camel", "monkey", "baboon"]

guess_word = r.choice(list_of_words)

wrong_guess = 0
display = ["_"] * len(guess_word)

while wrong_guess != 7:
    word_display = " ".join(display)

    print(word_display)

    user_guess = input("\nEnter your guess letter: ")
    split_word = list(guess_word)

    if user_guess not in guess_word:
        wrong_guess += 1
        print(hangman.stages[wrong_guess])
    elif user_guess in split_word:
        for i in range(len(split_word)):
            if user_guess == split_word[i]:
                display[i] = user_guess 

        if "_" not in display:
            print(f"correct it's {guess_word}")
            print("you win dude")
            break 
    else:
        if wrong_guess == 7:
            print("game over dude")
       
        
