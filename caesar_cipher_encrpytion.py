alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
]
selection = input("Type 'encode' to Encrypt your message, or 'decode' to decrypt your message: ")
text = input("Type your message: ")
shift = int(input("Type the shift number: "))


def encrypt(text, shift=0):
    cipher_text = ""

    for letter in text:
        shifted_position = alphabet.index(letter) + shift
        cipher_text += alphabet[shifted_position]

    print(f"Here is the encoded result: {cipher_text}")






encrypt(text=text, shift=shift)