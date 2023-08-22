def vigenere_encrypt(plaintext, key_stream):
    ciphertext = []
    
    for i, char in enumerate(plaintext):
        if char.isalpha():
            key = key_stream[i % len(key_stream)]
            shift = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift + key) % 26 + shift)
            ciphertext.append(encrypted_char)
        else:
            ciphertext.append(char)
    
    return ''.join(ciphertext)

def vigenere_decrypt(ciphertext, key_stream):
    plaintext = []
    
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            key = key_stream[i % len(key_stream)]
            shift = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - shift - key) % 26 + shift)
            plaintext.append(decrypted_char)
        else:
            plaintext.append(char)
    
    return ''.join(plaintext)

# Part (a) - Encryption
plaintext_a = "send more money"
key_stream_a = [9, 0, 1, 7, 23, 15, 21, 14, 11, 11, 2, 8, 9]
ciphertext_a = vigenere_encrypt(plaintext_a, key_stream_a)
print("Ciphertext (Part a):", ciphertext_a)

# Part (b) - Decryption
ciphertext_b = "ciph hxo ceedrc"
plaintext_b = "cash not needed"

# Find the key stream by subtracting the ASCII values of corresponding characters
key_stream_b = [(ord(ciphertext_b[i]) - ord(plaintext_b[i])) % 26 for i in range(len(plaintext_b))]
print("Key Stream (Part b):", key_stream_b)

# Decrypt using the found key stream
decrypted_b = vigenere_decrypt(ciphertext_b, key_stream_b)
print("Decrypted Text (Part b):", decrypted_b)
