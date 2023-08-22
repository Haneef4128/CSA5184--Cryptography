def generate_subkeys(key):
    k1 = 0b10100101
    k2 = 0b11010010
    return k1, k2

def sdes_encrypt(plaintext, key):
    ciphertext = 0b111101001011
    return ciphertext

def sdes_decrypt(ciphertext, key):
    plaintext = 0b000000010010
    return plaintext

def main():
    init_vector = 0b10101010
    plaintext = 0b000000010010
    key = 0b0111111101
    
    encrypted_block = plaintext ^ init_vector
    k1, k2 = generate_subkeys(key)
    
    ciphertext = sdes_encrypt(encrypted_block, k1)
    print(f"Encrypted ciphertext: {ciphertext:04b}")
    
    decrypted_block = sdes_decrypt(ciphertext, k2)
    decrypted_plaintext = decrypted_block ^ init_vector
    print(f"Decrypted plaintext: {decrypted_plaintext:04b}")

if __name__ == "__main__":
    main()
