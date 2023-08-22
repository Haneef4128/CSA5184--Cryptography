import numpy as np

def prepare_plaintext(plain_text, key_matrix):
    # Remove non-alphabetic characters and convert to uppercase
    plain_text = ''.join(filter(str.isalpha, plain_text)).upper()

    # If the length of the plain_text is not a multiple of the key matrix size, pad it with 'X'
    while len(plain_text) % key_matrix.shape[0] != 0:
        plain_text += 'X'

    return plain_text

def encrypt(plain_text, key_matrix):
    encrypted_text = ""
    n = key_matrix.shape[0]
    
    for i in range(0, len(plain_text), n):
        block = np.array([ord(char) - ord('A') for char in plain_text[i:i+n]])
        encrypted_block = np.dot(key_matrix, block) % 26
        encrypted_text += ''.join([chr(char + ord('A')) for char in encrypted_block])

    return encrypted_text

def main():
    key_matrix = np.array([[9, 4], [5, 7]])
    plain_text = "meet me at the usual place at ten rather than eight oclock"
    
    prepared_text = prepare_plaintext(plain_text, key_matrix)
    encrypted_text = encrypt(prepared_text, key_matrix)
    
    print("Plaintext:  ", plain_text)
    print("Encrypted: ", encrypted_text)

if __name__ == "__main__":
    main()
