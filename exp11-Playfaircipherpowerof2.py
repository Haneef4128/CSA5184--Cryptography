import math

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def calculate_possible_keys():
    total_possible_keys = factorial(25)
    return total_possible_keys

def calculate_effective_unique_keys():
    # Take into account symmetries: rotations and flips
    symmetries = 8  # 4 rotations * 2 flips
    total_possible_keys = calculate_possible_keys()
    effective_unique_keys = total_possible_keys // symmetries
    return effective_unique_keys

if __name__ == "__main__":
    possible_keys = calculate_possible_keys()
    effective_unique_keys = calculate_effective_unique_keys()

    print("Number of possible keys (ignoring symmetries):", possible_keys)
    print("Number of effectively unique keys (considering symmetries):", effective_unique_keys)
