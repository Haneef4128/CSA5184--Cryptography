class PolyalphabeticCipher:
    def __init__(self, key):
        self.key = key.upper()

    def extend_key(self, text):
        extended_key = self.key
        while len(extended_key) < len(text):
            extended_key += self.key
        return extended_key[:len(text)]

    def encrypt(self, plaintext):
        plaintext = plaintext.upper()
        extended_key = self.extend_key(plaintext)
        ciphertext = ''

        for i in range(len(plaintext)):
            if plaintext[i].isalpha():
                shift = ord(extended_key[i]) - ord('A')
                encrypted_char = chr(((ord(plaintext[i]) - ord('A') + shift) % 26) + ord('A'))
                ciphertext += encrypted_char
            else:
                ciphertext += plaintext[i]

        return ciphertext

    def decrypt(self, ciphertext):
        ciphertext = ciphertext.upper()
        extended_key = self.extend_key(ciphertext)
        plaintext = ''

        for i in range(len(ciphertext)):
            if ciphertext[i].isalpha():
                shift = ord(extended_key[i]) - ord('A')
                decrypted_char = chr(((ord(ciphertext[i]) - ord('A') - shift) % 26) + ord('A'))
                plaintext += decrypted_char
            else:
                plaintext += ciphertext[i]

        return plaintext

# Example usage
key = "KEY"  # You can provide your own key here
cipher = PolyalphabeticCipher(key)

plaintext = "HELLO, WORLD!"
encrypted_text = cipher.encrypt(plaintext)
print("Encrypted:", encrypted_text)

decrypted_text = cipher.decrypt(encrypted_text)
print("Decrypted:", decrypted_text)
