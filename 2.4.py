population = 620000
growth = 0.037
target = 1500000
year = 2024

while population <= target:
    population += population * growth
    year += 1

print(f"Население превысит 1,5 млн человек в {year} году.")