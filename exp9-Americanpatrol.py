def prepare_input(text):
    text = text.replace(" ", "").upper()
    return text

def find_char_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return -1, -1

def playfair_decrypt(ciphertext, key):
    decrypted_text = ""
    index = 0

    while index < len(ciphertext):
        char1 = ciphertext[index]
        char2 = ciphertext[index + 1]
        index += 2

        row1, col1 = find_char_position(key, char1)
        row2, col2 = find_char_position(key, char2)

        if row1 != -1 and row2 != -1:
            if row1 == row2:
                decrypted_text += key[row1][(col1 - 1) % 5] + key[row2][(col2 - 1) % 5]
            elif col1 == col2:
                decrypted_text += key[(row1 - 1) % 5][col1] + key[(row2 - 1) % 5][col2]
            else:
                decrypted_text += key[row1][col2] + key[row2][col1]
        else:
            decrypted_text += char1 + char2

    return decrypted_text

key = [
    ['K', 'X', 'J', 'E', 'Y'],
    ['U', 'R', 'E', 'B', 'Z'],
    ['W', 'H', 'T', 'F', 'S'],
    ['C', 'G', 'A', 'M', 'D'],
    ['P', 'Q', 'V', 'I', 'N']
]

ciphertext = "KXJEYUREBEZWEHEWRYTUHEYFSKREHEGOYFIWTTTUOLKSYCAJPOBOTEIZONTXBYBNTGONEYCUZWRGDSONSXBOUYWRHEBAAHYUSEDQ"

ciphertext = prepare_input(ciphertext)
decrypted_text = playfair_decrypt(ciphertext, key)

print("Decrypted:", decrypted_text)
