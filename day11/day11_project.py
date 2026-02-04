import os
import game_mechanics as game

computer_card_one = game.player_pick()
computer_card_two = game.player_pick()

print("WELCOME TO BLACK JACK CARD GAME")

continue_again = True
while continue_again == True:
    
    computer_cards_total = None
    player_cards_total = None

    start = input("Want to start the game (yes or no)?: ").lower()

    if start == "no":
        print("thank you for visiting!")
        break

    player_card_one = game.player_pick()
    player_card_two = game.player_pick()

    print(f"Here's the first Computer Card: \n{computer_card_one}")
    print(f"\nYour Card: \n{player_card_one}\n{player_card_two}")

    get_another_card = input("\nType 'y' to get another card, or 'no' to pass and see who wins? ").lower()

    if get_another_card[0] == "n":
        print(f"Here's the Computer two sets of Cards: \n{computer_card_one}\n{computer_card_two}")
        print(f"Your set of Cards: \n{player_card_one}\n{player_card_two}")

        computer_cards_total = game.total_value(computer_card_one, computer_card_two, None)
        player_cards_total = game.total_value(player_card_one, player_card_two, None)

    else:
        player_card_three = game.player_pick()
        print(f"Here's the Computer two sets of Cards: \n{computer_card_one}\n{computer_card_two}")
        print(f"\nNew card added to your deck of Cards: {player_card_three}")
        print(f"Your set of Cards: \n{player_card_one}\n{player_card_two}\n{player_card_three}")

        computer_cards_total = game.total_value(computer_card_one, computer_card_two, None)
        player_cards_total = game.total_value(player_card_one, player_card_two, player_card_three)
    
    print(game.who_wins(computer_cards_total, player_cards_total))
        
    try_again = input("\nWant to make another process (yes/no)? ")

    if try_again == "yes":
            os.system('cls')
            print("WELCOME TO BLACK JACK CARD GAME")
    else:
        print("thank you for playing, come again!")
        continue_again = False
        