
from googletrans import Translator
# Mapping of text characters to Braille ASCII
braille_ascii_mapping = {
    'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑', 'f': '⠋', 'g': '⠛', 'h': '⠓',
    'i': '⠊', 'j': '⠚', 'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕', 'p': '⠏',
    'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞', 'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭',
    'y': '⠽', 'z': '⠵', '1': '⠼⠁', '2': '⠼⠃', '3': '⠼⠉', '4': '⠼⠙', '5': '⠼⠑',
    '6': '⠼⠋', '7': '⠼⠛', '8': '⠼⠓', '9': '⠼⠊', '0': '⠼⠚', ',': '⠂', ';': '⠆',
    ':': '⠒', '.': '⠲', '!': '⠖', '?': '⠦', '-': '⠤', '(': '⠶', ')': '⠶', '"': '⠶',
    "'": '⠄', '#': '⠼', ' ': ' '
}

# Function to encode text to Braille ASCII
def text_to_braille_ascii(text):
    braille_text = ""
    for char in text.lower():
        braille_text += braille_ascii_mapping.get(char, '?')  # '?' for unknown chars
    return braille_text

# Function to decode Braille ASCII to text
def braille_ascii_to_text(braille_text):
    reverse_mapping = {v: k for k, v in braille_ascii_mapping.items()}
    text = ""
    skip = False
    for i, symbol in enumerate(braille_text):
        if skip:
            skip = False
            continue
        # Check for numeric prefix (⠼) for digits
        if symbol == '⠼' and i + 1 < len(braille_text):
            next_char = braille_text[i + 1]
            text += reverse_mapping.get('⠼' + next_char, '?')
            skip = True
        else:
            text += reverse_mapping.get(symbol, '?')
    return text

translator = Translator()

def translate_text(text, target_language):
  translation = translator.translate(text, dest=target_language)
  return translation.text
