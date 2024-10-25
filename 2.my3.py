n = int(input("Введите количество лет: "))
total_cost = 0
remaining_percent = 100
depreciation_rate = float(input("Введите процент уценки: ")) / 100

for i in range(n):
    cost = float(input(f"Введите стоимость оборудования за {i+1} год: "))
    total_cost += cost * remaining_percent
    remaining_percent *= (1 - depreciation_rate)

print(f"Общая стоимость накопленного оборудования за {n} лет: {total_cost:.2f}")