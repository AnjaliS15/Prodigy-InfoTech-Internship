alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encryption(plain_text,shift):
    cipher_text=''
    for char in plain_text:
        if char in alphabet: 
            position = alphabet.index(char)
            new_post = (position+shift)%26
            cipher_text += alphabet[new_post]
        else: 
            cipher_text += char
    print(f"Text after encryption: {cipher_text}")

def decryption(cipher_text,shift):
    plain_text=''
    for char in cipher_text:
        if char in alphabet: 
            position=alphabet.index(char)
            new_post=(position-shift)%26
            plain_text += alphabet[new_post]
        else: 
            plain_text += char
    print(f"Text after decryption: {plain_text}")

clear = False
while not clear:
    action = input("Type 'encrypt' for encr(yption and 'decrypt' for decryption: ")
    message = input("Your message: ").lower()
    shift = int(input("Enter the shift key value: "))

    if action=="encrypt":
        encryption(plain_text=message,shift=shift)
    elif action=="decrypt":
        decryption(cipher_text=message,shift=shift)

    go_again = input("Type 'yes' to continue and 'no' to exit: ")
    if go_again=='no':
        clear=True
        print("Thanks for using the tool!")