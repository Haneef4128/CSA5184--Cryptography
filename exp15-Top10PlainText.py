import string
from collections import Counter
import heapq

def caesar_decrypt(ciphertext, shift):
    decrypted_text = ''
    for char in ciphertext:
        if char.isalpha():
            shift_amount = -shift if char.isupper() else shift
            decrypted_char = chr(((ord(char) - ord('A') + shift_amount) % 26) + ord('A'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def letter_frequency_attack(ciphertext, num_top_plaintexts=10):
    frequencies = Counter(ciphertext)
    most_common = frequencies.most_common()
    
    possible_plaintexts = []
    for shift in range(26):
        potential_plaintext = caesar_decrypt(ciphertext, shift)
        score = sum(abs((frequencies.get(char, 0) / len(ciphertext)) - (expected_freq[char] / 100)) for char in string.ascii_uppercase)
        heapq.heappush(possible_plaintexts, (score, potential_plaintext))
    
    top_plaintexts = heapq.nsmallest(num_top_plaintexts, possible_plaintexts)
    return [(score, plaintext) for score, plaintext in top_plaintexts]

# English letter frequencies in percentages
expected_freq = {
    'A': 8.167, 'B': 1.492, 'C': 2.782, 'D': 4.253, 'E': 12.702, 'F': 2.228, 'G': 2.015,
    'H': 6.094, 'I': 6.966, 'J': 0.153, 'K': 0.772, 'L': 4.025, 'M': 2.406, 'N': 6.749,
    'O': 7.507, 'P': 1.929, 'Q': 0.095, 'R': 5.987, 'S': 6.327, 'T': 9.056, 'U': 2.758,
    'V': 0.978, 'W': 2.360, 'X': 0.150, 'Y': 1.974, 'Z': 0.074
}

ciphertext = "ZVMXOXQVOXJMZVYMKLJZVOXQVOXN"
num_top_plaintexts = 10

possible_plaintexts = letter_frequency_attack(ciphertext, num_top_plaintexts)
for score, plaintext in possible_plaintexts:
    print("Score:", score, "Plaintext:", plaintext)
