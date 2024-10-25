n = int(input("Введите натуральное число: "))
factor = 2

while n > 1:
    if n % factor == 0:
        print(factor, end = " ")
        n //= factor
    else:
        factor += 1