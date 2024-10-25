numbers = [1, 2, 3, 2, 4, 5, 6, 7, 8, 9, 7, 5, 5]
count = {}
for num in numbers:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1
for num, c in count.items():
    if c > 1:
        print(num)
