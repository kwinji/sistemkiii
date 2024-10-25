def format_list(items):
    if not items:
        return ''
    elif len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return f'{items[0]} и {items[1]}'
    else:
        return f"{', '.join(items[:-1])} и {items[-1]}"

# Получение списка от пользователя
user_input = input("Введите элементы списка, разделяя их пробелами: ").split(' ')
formatted = format_list(user_input)
# Вывод результата
print(f"Отформатированный список: {formatted}")