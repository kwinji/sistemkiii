numbers_ending_with_8 = [num for num in range(10, 100) if num * 2 % 10 == 8]


numbers_ending_with_4 = [num for num in range(10, 100) if num * 3 % 10 == 4]

print("Числа, которые при умножении на 2 заканчиваются на 8:", numbers_ending_with_8)
print("Числа, которые при умножении на 3 заканчиваются на 4:", numbers_ending_with_4)