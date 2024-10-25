A = int(input("Введите число А: "))
B = int(input("Введите число В: "))


if A >= B:
    print("Ошибка: A должно быть меньше B")
else:

    sum_squares = 0
    for i in range(A, B + 1):
        sum_squares += i ** 2

    print(f"Сумма квадратов всех целых чисел от {A} до {B} включительно: {sum_squares}")