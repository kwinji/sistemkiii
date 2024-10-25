filename = input("Введите имя файла: ")

with open(filename, 'w') as file:
    print("Начните вводить строки (нажмите Enter для завершения):")

    while True:
        line = input("> ")
        if line == "":
            break
        file.write(line + "\n")

print("Файл записан.")