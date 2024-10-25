a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

if a % 2 == 0:
    a = a / 2
elif a == 1:
    a = 2

if b % 2 == 0:
    b = b / 2
elif b == 1:
    b = 2

if c % 2 == 0:
    c = c / 2
elif c == 1:
    c = 2

print("Первое число:", a)
print("Второе число:", b)
print("Третье число:", c)