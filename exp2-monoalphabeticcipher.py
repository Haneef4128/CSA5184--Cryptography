class MonoalphabeticCipher:
    def __init__(self, key=None):
        if key:
            self.key = key.upper()
        else:
            self.key = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'  # Default key as reverse alphabet

    def encrypt(self, plaintext):
        plaintext = plaintext.upper()
        ciphertext = ''
        for char in plaintext:
            if char.isalpha():
                idx = ord(char) - ord('A')
                ciphertext += self.key[idx]
            else:
                ciphertext += char

        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = ''
        for char in ciphertext:
            if char.isalpha():
                idx = self.key.index(char)
                plaintext += chr(idx + ord('A'))
            else:
                plaintext += char

        return plaintext

# Example usage
key = "KJFABSWVURMTOHECXDYPLQGNIZ"  # You can provide your own key here
cipher = MonoalphabeticCipher(key)

plaintext = "HELLO, WORLD!"
encrypted_text = cipher.encrypt(plaintext)
print("Encrypted:", encrypted_text)

decrypted_text = cipher.decrypt(encrypted_text)
print("Decrypted:", decrypted_text)
