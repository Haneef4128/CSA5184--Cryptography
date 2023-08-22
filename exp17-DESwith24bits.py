def permute(input, table):
    result = 0
    for i in range(len(table)):
        result |= ((input >> (64 - table[i])) & 1) << (len(table) - 1 - i)
    return result

def des_decrypt(ciphertext, key):
    IP = [2, 6, 3, 1, 4, 8, 5, 7]
    IP_INV = [4, 1, 3, 5, 7, 2, 8, 6]

    permuted_ciphertext = permute(ciphertext, IP)
    decrypted = permuted_ciphertext ^ key
    decrypted = permute(decrypted, IP_INV)

    return decrypted

def main():
    KEY = 0x133457799BBCDFF1
    CIPHERTEXT = 0x0123456789ABCDEF

    decrypted = des_decrypt(CIPHERTEXT, KEY)

    print(f"Ciphertext: {CIPHERTEXT:016X}")
    print(f"Decrypted:  {decrypted:016X}")

if __name__ == "__main__":
    main()
