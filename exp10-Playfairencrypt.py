def find_position(matrix, letter):
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if col == letter:
                return (i, j)
    return (-1, -1)

def playfair_encrypt(matrix, plaintext):
    ciphertext = ""
    
    # Prepare the plaintext: convert to uppercase, replace J with I, remove punctuation and spaces
    plaintext = plaintext.upper().replace("J", "I").replace(".", "").replace(" ", "")
    
    # Break the plaintext into digraphs
    i = 0
    digraphs = []
    while i < len(plaintext):
        if i == len(plaintext) - 1:
            digraphs.append(plaintext[i] + "X")
            i += 1
        elif plaintext[i] == plaintext[i + 1]:
            digraphs.append(plaintext[i] + "X")
            i += 1
        else:
            digraphs.append(plaintext[i] + plaintext[i + 1])
            i += 2

    for digraph in digraphs:
        row1, col1 = find_position(matrix, digraph[0])
        row2, col2 = find_position(matrix, digraph[1])
        
        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2] + matrix[row2][col1]
    
    return ciphertext

matrix = [
    ['M', 'F', 'H', 'I', 'K'],
    ['U', 'N', 'O', 'P', 'Q'],
    ['Z', 'V', 'W', 'X', 'Y'],
    ['E', 'L', 'A', 'R', 'G'],
    ['D', 'S', 'T', 'B', 'C']
]

plaintext = "Must see you over Cadogan West. Coming at once."
ciphertext = playfair_encrypt(matrix, plaintext)
print("CipherText : ", ciphertext)
