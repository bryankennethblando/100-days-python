import random as r
import os


actors_followers = [
    {"name": "Selena Gomez", "followers": "415M"},
    {"name": "Dwayne Johnson", "followers": "390M"},
    {"name": "Ariana Grande", "followers": "372M"},
    {"name": "Jennifer Lopez", "followers": "246M"},
    {"name": "Kevin Hart", "followers": "176M"},
    {"name": "Zendaya", "followers": "175M"},
    {"name": "Gal Gadot", "followers": "106M"},
    {"name": "Vin Diesel", "followers": "105M"},
    {"name": "Shraddha Kapoor", "followers": "95M"},
    {"name": "Priyanka Chopra", "followers": "94M"}
]

def parse_followers(follower_str):
    return int(follower_str.replace("M", ""))

def game_restart(try_again):
    if try_again == "y":
        return True
    else:
        return False
    
def artist_comparison(choice, current_life, followers_a, followers_b, name_a, name_b):
    is_correct = False
    if (followers_a > followers_b and choice == "h") or (followers_a < followers_b and choice == "l"):
        print(f"correct Artist {name_a} has more followers than Artist {name_b}")
        is_correct = True
    else:
        print(f"false Artist {name_a} does not match your guess compared to Artist {name_b}")
        current_life -= 1
        print(f"you have {current_life} left to guess.")
    return is_correct, current_life

print("you have 10 rounds, but only have 5 user lives to have")
print("make sure to guess all correctly to clear the game")

continue_again = True
while continue_again:
    user_life = 5
    rounds = 1
    
   
    while user_life > 0 and rounds <= 10:
        artist_a = r.randint(0, len(actors_followers) - 1) 
        artist_b = r.randint(0, len(actors_followers) - 1) 

        while artist_a == artist_b:
            artist_b = r.randint(0, len(actors_followers) - 1) 
            
        artist_a_name = actors_followers[artist_a]['name']
        artist_b_name = actors_followers[artist_b]['name']

        print(f"\nRound {rounds}")
        print(f"Artist A: {artist_a_name}")
        print(f"Artist B: {artist_b_name}")
        comparison = input("\ntype 'h' if artist A has more followers than artist B, and 'l' if not: ")

        artist_a_followers = parse_followers(actors_followers[artist_a]['followers'])
        artist_b_followers = parse_followers(actors_followers[artist_b]['followers'])

      
        is_true, user_life = artist_comparison(comparison, user_life, artist_a_followers, artist_b_followers, artist_a_name, artist_b_name)
        
        rounds += 1

  
    if user_life > 0:
        print("\ncongratulations you've cleared the game!")
    else:
        print(f"\nsorry you lose after {rounds - 1} rounds")

   
    user_reply = input("\nWant to try again (y/n): ").lower()
    if game_restart(user_reply):
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        continue_again = False