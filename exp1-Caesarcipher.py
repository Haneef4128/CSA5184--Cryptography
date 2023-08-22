def caesar_cipher(text, key):
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            shift = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - shift + key) % 26 + shift)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char

    return encrypted_text

# Example usage
plaintext =input("enter the text:")
key = int(input("enter the key value:"))
encrypted_text = caesar_cipher(plaintext, key)
print("Encrypted:", encrypted_text)
