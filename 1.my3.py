number = int(input("Введите трехзначное число: "))

if number < 100 or number >= 1000:
    print("Число должно быть трехзначным!")
    exit()

sum_of_digits = 0
temp_number = number
while temp_number > 0:
    sum_of_digits += temp_number % 10
    temp_number //= 10

if sum_of_digits % 3 == 0:
    print(f"Число {number} делится на 3.")
else:
    print(f"Число {number} не делится на 3.")