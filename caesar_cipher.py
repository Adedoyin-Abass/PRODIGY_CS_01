def caesar_cipher(text, shift, mode):

    result = ""

    # Normalize shift to be within 0-25
    shift = shift % 26

    # For Decryption, shift in the opposite direction
    if mode == 'decrypt':
        shift = 26 - shift

    for char in text:
        # For lowercase letters
        if 'a' <= char <= 'z':
            start_ascii = ord('a')
            shifted_char_ascii = (ord(char) - start_ascii + shift) % 26 + start_ascii
            result += chr(shifted_char_ascii)
        # For UPPERCASE letters
        elif 'A' <= char <= 'Z':
            start_ascii = ord('A')
            shifted_char_ascii = (ord(char) - start_ascii + shift) % 26 + start_ascii
            result += chr(shifted_char_ascii)
        # To keep non-alphanumeric characters as they are
        else:
            result += char
    return result

# Main Function
def main():
    print("Caesar Cipher Program")
    message = input("Enter your message: ")

    while True:
        try:
            shift_input = input("Enter the shift value (an integer): ")
            shift = int(shift_input)
            break # Stop loop if input is an integer
        except ValueError:
            print("Invalid shift value. Please enter an integer")

    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt? (e/d): ").lower()
        if choice in ['e','d']:
            break # Stop loop if choice is valid
        else:
            print("invalid choice. Please enter 'e' for encrypt or 'd' for decrypt")

    if choice == 'e':
        encrypted_message = caesar_cipher(message, shift, 'encrypt')
        print(f"\nOriginal Message: {message}")
        print(f"Shift Value: {shift}")
        print(f"\nEncrypted Message: {encrypted_message}")
    else:
        decrypted_message = caesar_cipher(message, shift, 'decrypt')
        print(f"\nOriginal Message:{message}")
        print(f"Shift Value: {shift}")
        print(f"\nDecrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()




