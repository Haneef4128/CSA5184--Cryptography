def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def affine_caesar_encrypt(text, a, b):
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((a * (ord(char) - shift) + b) % 26 + shift)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char

    return encrypted_text

def affine_caesar_decrypt(ciphertext, a, b):
    mod_inv = mod_inverse(a, 26)
    if mod_inv is None:
        return "Error: 'a' value is not valid (no modular inverse exists)"

    decrypted_text = ""

    for char in ciphertext:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((mod_inv * ((ord(char) - shift) - b)) % 26 + shift)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char

    return decrypted_text

# Main program
plaintext = input("Enter the text:")
a = int(input("Enter the A value:"))
b = int(input("Enter the B value:"))

encrypted_text = affine_caesar_encrypt(plaintext, a, b)
print("Encrypted:", encrypted_text)

decrypted_text = affine_caesar_decrypt(encrypted_text, a, b)
print("Decrypted:", decrypted_text)
