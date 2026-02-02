# Creating a Silent Auction Bid using Dict
import os 

people_in_room = {}

def getting_bid (name, bid):
    people_in_room[name] = bid


is_there_bidders = True
while is_there_bidders == True:

    name = input("What is your Name: ")
    bid = int(input("What's your Bid: $"))

    getting_bid(name, bid)

    any_bidders = input("Are they any other Bidders (yes or no)? ").lower()

    if any_bidders == "yes":
        os.system('cls')
    else:
        is_there_bidders = False
    
winner_name = " "
winner_bid = 0
for key, value in people_in_room.items():
   
    if value > winner_bid:
        winner_name = key
        winner_bid = value
print(f"The Bid winner is {winner_name} with a bid of ${winner_bid}.")
