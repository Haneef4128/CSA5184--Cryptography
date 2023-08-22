import numpy as np

def hill_decrypt(key_matrix, ciphertext):
    key_matrix = np.array(key_matrix)
    inverse_key_matrix = np.linalg.inv(key_matrix)
    
    n = len(key_matrix)
    plaintext = ''
    
    for i in range(0, len(ciphertext), n):
        block = [ord(char) - ord('A') for char in ciphertext[i:i+n]]
        block = np.array(block)
        decrypted_block = np.dot(inverse_key_matrix, block) % 26
        plaintext += ''.join([chr(int(num) + ord('A')) for num in decrypted_block])
    
    return plaintext

# Known plaintext-ciphertext pairs
known_pairs = [
    ("meet", "TCZU"),
    ("test", "CTAT")
]

# Attack: Recover the key matrix using known pairs
recovered_key_matrix = []
for plain, cipher in known_pairs:
    plain_block = [ord(char) - ord('A') for char in plain]
    cipher_block = [ord(char) - ord('A') for char in cipher]
    
    # Calculate the difference between cipher and plain blocks
    difference_block = (np.array(cipher_block) - np.array(plain_block)) % 26
    
    recovered_key_matrix.append(difference_block)

# Calculate the average difference matrix to recover the key matrix
recovered_key_matrix = np.array(recovered_key_matrix)
average_difference_matrix = np.mean(recovered_key_matrix, axis=0)
recovered_key_matrix = (average_difference_matrix % 26).reshape(2, 2)

print("Recovered Key Matrix:")
print(recovered_key_matrix)

# Decrypt ciphertext using the recovered key matrix
ciphertext = "TCZUCTAT"
recovered_plaintext = hill_decrypt(recovered_key_matrix, ciphertext)
print("Recovered Plaintext:", recovered_plaintext)
