alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
            ]
from art import logo

print(logo)
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your Messege:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    def ceaser(text, shift):
        if direction == "encode":
            cipher_text = ""
            for letter in text:
                if letter in alphabet:
                    position = alphabet.index(letter)
                    new_position = position + shift
                    new_letter = alphabet[new_position]
                    cipher_text += new_letter
                else:
                    cipher_text += letter
            print(f"The encoded text is: {cipher_text}")

        if direction == "decode":
            cipher_text = ""
            end_text = ""
            for letter in text:
                if letter in alphabet:
                    position = alphabet.index(letter)
                    new_position = position - shift
                    new_letter = alphabet[new_position]
                    cipher_text += new_letter
                else:
                    cipher_text += letter
            print(f"The encoded text is: {cipher_text}")


    ceaser(text, shift)
    result = input("Type yes if want to go again. Otherwise type no\n")
    if result == "no":
        should_continue = False
        print("GoodBye")



