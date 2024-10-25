input_filename = input("Введите имя входного файла: ")
max_lines = int(input("Введите максимальное количество строк: "))

with open(input_filename, 'r') as file:
    lines = file.readlines()

file_count = 1
line_count = 0

for i in range(0, len(lines), max_lines):
    output_filename = f"{file_count}.txt"

    with open(output_filename, 'w') as output_file:
        output_file.writelines(lines[i:i + max_lines])

    file_count += 1

print("Файлы успешно созданы.")