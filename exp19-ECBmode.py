from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import random

def pad(data):
    padder = padding.PKCS7(128).padder()
    return padder.update(data) + padder.finalize()

def unpad(data):
    unpadder = padding.PKCS7(128).unpadder()
    return unpadder.update(data) + unpadder.finalize()

# Generate a random 16-byte encryption key
key = b'0123456789abcdef'

# Original plaintext blocks
P1 = b"This is block P1"
P2 = b"This is block P2"
P3 = b"This is block P3"

# Encryption in ECB mode
cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
encryptor = cipher.encryptor()

C1 = encryptor.update(pad(P1)) + encryptor.finalize()
print(f"C1: {C1.hex()}")

# Simulate a bit error in P1
error_position = random.randint(0, len(P1) - 1)
P1_with_error = bytearray(P1)
P1_with_error[error_position] ^= 1

# Encrypt P2
encryptor = cipher.encryptor()
C2 = encryptor.update(pad(P2)) + encryptor.finalize()
print(f"C2: {C2.hex()}")

# Decryption in ECB mode
decryptor = cipher.decryptor()

# Decrypt C1
decrypted_P1 = unpad(decryptor.update(C1) + decryptor.finalize())
print(f"Decrypted P1: {decrypted_P1.decode()}")

# Create a new decryptor for C2
decryptor = cipher.decryptor()

# Simulate an error in C1 affecting C2
error_position = random.randint(0, len(C1) - 1)
C1_with_error = bytearray(C1)
C1_with_error[error_position] ^= 1

# Decrypt C2 using the modified C1
decrypted_P2 = unpad(decryptor.update(C2) + decryptor.finalize())
print(f"Decrypted P2: {decrypted_P2.decode()}")
