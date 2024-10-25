n = int(input("Введите натуральное число: "))
sumdel = 0

for i in range(1, n + 1):
    if n % i == 0 and i % 2 != 0:
        sumdel += i

print("Сумма нечетных делителей равна", sumdel)
