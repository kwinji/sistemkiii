import math
def solve_quadratic_equation(a, b, c):

    # Проверяем, что коэффициент при второй степени неизвестного не равен 0
    if a == 0:
        print("Коэффициент при второй степени неизвестного равен 0. Это не квадратное уравнение.")
        return None, None

    # Вычисляем дискриминант
    discriminant = b ** 2 - 4 * a * c

    # Если дискриминант отрицательный, корней нет
    if discriminant < 0:
        print("Дискриминант отрицательный, действительных корней нет.")
        return None, None

    # Вычисляем корни
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)

    return x1, x2


# Получаем коэффициенты уравнения от пользователя
a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

# Решаем уравнение
x1, x2 = solve_quadratic_equation(a, b, c)

# Выводим результаты
if x1 is not None and x2 is not None:
    print(f"Корни уравнения: x1 = {x1:.2f}, x2 = {x2:.2f}")