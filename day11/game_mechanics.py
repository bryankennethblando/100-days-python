# Creating a black jack game
import random as r

suits_of_cards = ["Diamonds", "Clubs", "Hearts", "Spades"]
card_name = ["Ace", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
card_value = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

ranks = dict(zip(card_name, card_value))
set_of_cards = {suit: ranks for suit in suits_of_cards}

def random_pick():
    random_suits = r.choice(list(set_of_cards.keys()))
    random_card = r.choice(list(set_of_cards[random_suits].keys()))
    random_value = set_of_cards[random_suits][random_card]
    return random_suits, random_card, random_value

def player_pick():
    suits, card, value = random_pick()
    return f"{suits} card {card} value: {value}"

def total_value(card_one, card_two, card_three):

    if card_one[-2 : ] == "11":
        first_card_value = int(card_one[-2 : ])
    else:
        first_card_value = int(card_one[-1])

    if card_two[-2 : ] == "11":
        second_card_value = int(card_two[-2 : ])
    else:
        second_card_value = int(card_two[-1])
    
    if card_three is None:
        return first_card_value + second_card_value
    else: 
        if  card_three[-2 : ] == "11":
            third_card_value = int(card_three[-2 : ])
            return first_card_value + second_card_value + third_card_value
        else: 
            third_card_value = int(card_three[-1])
            return first_card_value + second_card_value + third_card_value

def who_wins(player1, player2):
    if player2 > 21:
        return "\tYou went over 21. Computer Wins!"
    elif player1 > 21:
        return "\tComputer went over 21. You Win!"
    elif player1 == player2:
        return "\tIt's a Draw!"
    elif player2 > player1:
        return "\tCongratulations You Win!"
    elif player1 > player2:
        return "\tCongratulations Computer Wins!"