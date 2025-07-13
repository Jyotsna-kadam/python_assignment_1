# Assignment: Text to Morse Code Converter 

# Morse Code Dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.',   'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-',  'L': '.-..',
    'M': '--',  'N': '-.',   'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-',    'U': '..-',
    'V': '...-', 'W': '.--',  'X': '-..-',
    'Y': '-.--', 'Z': '--..',

    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----',

    ',': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.',  '-': '-....-', '(': '-.--.',
    ')': '-.--.-', ' ': '/'
}

text = input("Enter your message: ").upper()

morse_code = ""
for letter in text:
    if letter in MORSE_CODE_DICT:
        morse_code += MORSE_CODE_DICT[letter] + " "
    else:
        morse_code += "? "

print(f"Morse Code: {morse_code}")

