D-Encryptor

D-Encryptor is a Python-based GUI tool for message encryption and decryption using cryptographic techniques such as Caesar Cipher, Vigenère Cipher, and Columnar Transposition Cipher.
Features

    Encrypt and decrypt text using:

        Caesar Cipher

        Vigenère Cipher (with a fixed key: tractor)

        Row-Column Transposition Cipher

    GUI built with tkinter

    Displays:

        ASCII conversions

        Matrix manipulations

        Detailed intermediate steps in the console

Requirements

    Python 3.x

    Python packages:

        numpy

        tkinter (usually included with Python)

How to Run

    Clone this repository:

```bash
git clone https://github.com/yourusername/D-Encryptor.git
cd D-Encryptor
```

Run the script:

```bash
    python your_script_name.py
```
    The GUI will open. Enter your message, choose an encryption method, and click Encrypt or Decrypt.

Note:
The GUI currently contains placeholder button functions (ButtonTest). You will need to link them to the actual encryption functions like CaesarCipher, VigenereCipher, or RowColumnTCipher.
Supported Algorithms
Caesar Cipher

A shift-based encryption method where each character is shifted by a fixed number of positions.
Key used: 6
Vigenère Cipher

A polyalphabetic substitution cipher using a repeating key.
Key used: "tractor"
Row-Column Transposition Cipher

Reorders characters into a matrix and sorts the columns based on a key.
Key used: [5, 2, 6, 1]
Example Usage (Command Line)

n = message()
ascii_array = Text2ASCII(n)
encrypted = CaesarCipher(ascii_array)
OutputMessage(encrypted)

To Do

    Link encryption and decryption logic to the GUI buttons

    Add user-defined key input support for Caesar and Vigenère ciphers

    Improve error handling and input validation

    Enhance the GUI layout and usability

GUI Preview

![Screenshot of GUI](images/GUI.png)
