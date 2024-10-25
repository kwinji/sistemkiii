x = float(input("Введите координату x: "))
y = float(input("Введите координату y: "))

in_semicircle = (x <= 0) and (x**2 + y**2 <= 1)

in_square = (0 <= x <= 1) and (0 <= y <= 1)

if in_semicircle or in_square:
    print("Точка находится в заштрихованной области.")
else:
    print("Точка не находится в заштрихованной области.")