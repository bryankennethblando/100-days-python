#creating a caesar cipher
import string
set_of_letters = list(string.ascii_lowercase)

def caesar(word, shift, direction):
    #refractor
    letters_in_word = list(word)
    encrypt = []
   
    for letter in letters_in_word:
            if letter in set_of_letters:
                current_pos = set_of_letters.index(letter)
                if direction == "encrypt":

                    index_found = (current_pos + shift) % 26

                elif direction == "decrypt":

                    index_found = (current_pos - shift) % 26

                new_letter = set_of_letters[index_found]
                encrypt.append(new_letter)

            else:
                encrypt.append(letter)

    word = "".join(encrypt)
    if direction == "encrypt":

        print(f"Encoded message: {word}")

    elif direction == "decrypt":

        print(f"Decoded message: {word}")


try_again = True  
while try_again == True:
    direction = input("Type to encode to 'encrypt' and decode to 'decrypt': ").lower()
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    caesar(text, shift, direction)
    
    repeat = input("want to try again (yes or no)? ").lower()
    
    if repeat == "no":
        try_again = False


   

