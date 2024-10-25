import random

numbers = [random.randint(1, 10) for _ in range(10)]
print("Исходный список:", numbers)

numbers = [num ** 2 for num in numbers]
print("Список с квадратами:", numbers)