for num in range(1000, 10000):
    str_num = str(num)
    first = int(str_num[0])
    second = int(str_num[1])
    third = int(str_num[2])
    fourth = int(str_num[3])

    if (first + fourth) == (second + third):
        print(num)