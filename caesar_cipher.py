import string
from operator import truediv

alphabet_list = list(string.ascii_lowercase)

def caesar(original_text,shift_amount,encode_decode):
    output_text = ""
    if encode_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet_list:
            output_text += letter

        else:
                shifted_position = alphabet_list.index(letter) + shift_amount
                shifted_position %= len(alphabet_list)
                output_text += alphabet_list[shifted_position]

    print(f"Your {encode_decode}ed message is: {output_text}")

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text = text, shift_amount=shift,encode_decode=direction)

    result = input("Do you want to continue? 'Yes' or 'no' ").lower()

    if result == "no":
        should_continue = False
        print("Bye")