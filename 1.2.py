def main():
    print("Введите длины сторон треугольника:")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    if a == b == c:
        print("Равносторонний треугольник")
    elif a == b or a == c or b == c:
        print("Равнобедренный треугольник")
    else:
        print("Разносторонний треугольник")
main()