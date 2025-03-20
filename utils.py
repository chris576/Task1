# Ersetzt auch bereits ersetzte Strings aus dem Dict. Aber wie verhindere ich das? 
from copy import deepcopy

def get_longest_value(combinde_dict):
    longest_value = 1
    for k in combinde_dict:
        if len(combinde_dict[k]) > longest_value:
            longest_value = len(combinde_dict[k])
    return longest_value

import re

def read_and_clean_text(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    
    # Alle Sonderzeichen und Leerzeichen entfernen, nur Großbuchstaben beibehalten
    cleaned_text = re.sub(r'[^A-Z]', '', text.upper())
    
    return cleaned_text

def group_in_blocks(string, block_size):
    # Teile den String in Blöcke der gewünschten Größe
    blocks = [string[i:i+block_size] for i in range(0, len(string), block_size)]
    # Füge die Blöcke mit Leerzeichen zusammen
    grouped_string = ' '.join(blocks)
    return grouped_string