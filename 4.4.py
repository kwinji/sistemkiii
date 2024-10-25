input_files = input("Введите имена файлов для объединения (через пробел): ").split()
output_filename = input("Введите имя выходного файла: ")

with open(output_filename, 'w') as output_file:
    for input_file in input_files:
        with open(input_file, 'r') as file:
            output_file.write(file.read())
            output_file.write("\n")

print(f"Файлы успешно объединены в {output_filename}.")