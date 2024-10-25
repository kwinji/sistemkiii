def main():
    print("Введите ваш рост (в см):")
    height = float(input())

    optw = height - 100

    print("Введите ваш вес (в кг):")
    weight = float(input())

    if weight > optw:
        print("Вам нужно снизить вес.")
    elif weight < optw:
        print("Вам нужно набрать вес.")
    else:
        print("Ваш вес соответствует оптимальному.")
main()