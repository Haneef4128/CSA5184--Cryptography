def playfair_decrypt(key, message):
    key = key.replace(" ", "").upper()  # Remove spaces and convert to uppercase
    key_matrix = [[key[i + j*5] for i in range(5)] for j in range(5)]
    
    message = message.replace(" ", "").upper()
    decrypted = ""
    i = 0
    
    while i < len(message):
        char1, char2 = message[i], message[i+1]
        
        row1, col1 = None, None
        row2, col2 = None, None
        
        for r in range(5):
            if char1 in key_matrix[r]:
                row1, col1 = r, key_matrix[r].index(char1)
            if char2 in key_matrix[r]:
                row2, col2 = r, key_matrix[r].index(char2)
        
        # Handle cases where characters are not found in the key matrix
        if row1 is None or col1 is None or row2 is None or col2 is None:
            decrypted += " "
        else:
            if row1 == row2:
                decrypted += key_matrix[row1][(col1 - 1) % 5] + key_matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                decrypted += key_matrix[(row1 - 1) % 5][col1] + key_matrix[(row2 - 1) % 5][col2]
            else:
                decrypted += key_matrix[row1][col2] + key_matrix[row2][col1]
        
        i += 2
    
    return decrypted

key = 'K E Y F S T U X J H B N O P C A G V W R I L D Q Z W M'
message = 'KXJEY UREBE ZWEHE WRYTU HEYFS KREHE GOYFI WTTTU OLKSY CAJPO BOTEI ZONTX BYBNT GONEY CUZWR GDSON SXBOU YWRHE BAAHY USEDQ'
print("Message:",message)
decrypted = playfair_decrypt(key, message)
print("\nDecrypt:",decrypted)
