n = int(input("Введите количество делителей: "))

for num in range(1, 201):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
    if count == n:
        print(num)