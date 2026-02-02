# We're creating a rock, paper, and scissor game 
import random as r

game_choices = [
    # Rock (Index 0)
    """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    """,

    # Paper (Index 1)
    """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
    """,

    # Scissors (Index 2)
    """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    """
]

user_choice =  int(input("What do you choose? Type 1 for rock, 2 for paper, 3 for scissor: "))
computer_pick = r.randint(0, 2)

# showing the pick
print (f"Your pick: \n{game_choices[user_choice - 1]}")
print (f"\nComputer's pick: \n{game_choices[computer_pick]}")

# condition: checking who wins
if game_choices[computer_pick] == game_choices[user_choice - 1]:
    print ("It's a tie.")
elif game_choices[user_choice - 1] == 0  and game_choices[computer_pick] == 2:
    print ("You win.")
elif game_choices[user_choice - 1] == 1 and game_choices[computer_pick] == 0:
    print ("You win.")
elif game_choices[user_choice - 1] == 2 and game_choices[computer_pick] == 1:
    print ("You win.")
else:
    print ("You lose.")
   