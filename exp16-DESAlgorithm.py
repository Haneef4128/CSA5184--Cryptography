p8 = [6, 7, 8, 9, 1, 2, 3, 4]
p10 = [6, 7, 8, 9, 10, 1, 2, 3, 4, 5]

input = input("Enter 10 bits input:")
input = input[:10]

temp = ""
for i in range(10):
    cnt = p10[i]
    temp += input[cnt-1]

print("\nYour p10 key is    :", p10)
print("Bits after p10     :", temp)

LS1 = temp[1:] + temp[0]
LS2 = temp[2:] + temp[:2]
print("Output after LS-1  :", LS1)

print("\nYour p8 key is     :", p8)

k1 = ""
for i in range(8):
    cnt = p8[i]
    k1 += LS1[cnt-1]

print("Your key k1 is     :", k1)
