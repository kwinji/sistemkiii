distance_first_day = float(input("Введите расстояние, пройденное в первый день (в км): "))

days = int(input("Введите количество дней: "))

distance_last_day = distance_first_day * (1.1 ** (days-1))

print(f"На {days}-й день спортсмен пробежал {distance_last_day:.2f} км.")