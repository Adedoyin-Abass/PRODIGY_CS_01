# PRODIGY_CS_01
Caesar Cipher Program

This is a simple Python program that implements the classic Caesar Cipher. It allows you to encrypt or decrypt messages by shifting letters a certain number of positions down or up the alphabet.

## Features
* Encryption: Transform your plain text into a secret message.
* Decryption: Revert an encrypted message back to its original form.
* Case-Preserving: Handles both uppercase and lowercase letters correctly.
* Non-Alphabetic Character Handling: Leaves numbers, symbols, and spaces unchanged.
* User-Friendly Interface: Simple prompts for message, shift value, and mode (encrypt/decrypt).

## How it Works (The Caesar Cipher)
The Caesar Cipher is one of the simplest and most widely known encryption techniques. It's a type of substitution cipher where each letter in the plaintext is replaced by a letter some fixed number of positions down or up the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on.

# Getting Started
## Prerequisites
You only need Python 3 installed on your system to run this program.

## Installation
* Clone the repository (or copy the code into a .py file):

Open `Bash`
Type `git clone https://github.com/Adedoyin-Abass/PRODIGY_CS_01.git`
`cd PRODIGY_CS_01`

* Save the code: If you're not cloning, save the provided Python code into a file named `caesar_cipher.py` (or any other .py extension).

## Running the Program
Open your terminal or command prompt, navigate to the directory where you saved the file, and run:

Open `Bash`
Then input `python caesar_cipher.py`
The program will then guide you through the process:
* Enter your message.
* Enter the shift value (an integer).
* Choose to `(e)ncrypt` or `(d)ecrypt`.
![Alt text](https://github.com/Adedoyin-Abass/PRODIGY_CS_01/blob/main/Screenshots/un.png)

## Code Explanation
The core logic resides in the Caesar_cipher function:

* `shift = shift % 26`: This normalizes the shift value so that it's always between 0 and 25. A shift of 27 is the same as a shift of 1, for example.
* `if mode == 'decrypt': shift = 26 - shift`: For decryption, we essentially perform an encryption with the opposite shift. Shifting "forward" by X for encryption is undone by shifting "forward" by `26 - X` for decryption (which is effectively shifting "backward" by X).
* `ord(char) - start_ascii`: This converts a letter to its 0-25 alphabet index (e.g., 'a' becomes 0, 'b' becomes 1).
* `shift) % 26`: Applies the shift and uses the modulo operator (% 26) to "wrap around" the alphabet. If you shift 'z' by 1, it becomes 'a'.
* `start_ascii`: Converts the 0-25 alphabet index back to its ASCII value.
* `chr(shifted_char_ascii):` Converts the ASCII value back to a character.

![Alt text](https://github.com/Adedoyin-Abass/PRODIGY_CS_01/blob/main/Screenshots/trois.png)
![Alt text](https://github.com/Adedoyin-Abass/PRODIGY_CS_01/blob/main/Screenshots/deux.png)

## Contributing
Feel free to fork this repository, make improvements, and submit pull requests. Any contributions are welcome!

## License
This project is open source and available under the MIT License.

## Author
Adedoyin Abass / https://github.com/Adedoyin-Abass
