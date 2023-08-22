def permute(input, table, size):
    result = 0
    for i in range(size):
        result |= ((input >> (64 - table[i])) & 1) << (size - 1 - i)
    return result

def generate_subkeys(key):
    PC1 = [
        57, 49, 41, 33, 25, 17, 9, 1,
        58, 50, 42, 34, 26, 18, 10, 2,
        59, 51, 43, 35, 27, 19, 11, 3,
        60, 52, 44, 36, 63, 55, 47, 39,
        31, 23, 15, 7, 62, 54, 46, 38,
        30, 22, 14, 6, 61, 53, 45, 37,
        29, 21, 13, 5, 28, 20, 12, 4
    ]
    PC2 = [
        14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32
    ]
    key = permute(key, PC1, 56)
    subkeys = []
    for i in range(16):
        shifted_key = ((key << i) | (key >> (28 - i))) & 0xFFFFFFFFFFFFFFF  # To ensure 56 bits
        subkey = permute(shifted_key, PC2, 48)
        subkeys.append(subkey)
    return subkeys

def main():
    KEY = 0x0000FFFFFFFFFFFF
    subkeys = generate_subkeys(KEY)

    print("Generated Subkeys:")
    for i, subkey in enumerate(subkeys):
        print(f"K{i + 1}: 0x{subkey:012X}")

if __name__ == "__main__":
    main()
