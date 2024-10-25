decnumber = int(input("Введите число от 0 до 255: "))

if 0 <= decnumber < 256:
    if decnumber == 0:
        binnumber = "0"
    else:
        binnumber = ""

        while decnumber > 0:
            binnumber = str(decnumber % 2) + binnumber
            decnumber //= 2

    print(f"Двоичное представление числа = {binnumber}")
else:
    print("Число должно быть в диапазоне от 0 до 255.")
