import _thread
import socket

# Функция для получения сообщений от сервера
def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
        except:
            print("Error receiving message.")
            client_socket.close()
            break

# Настройка клиента
def start_client():
    host = socket.gethostname()  # Локальный хост
    port = 12345  # Порт

    client_socket.connect((host, port))

    print(f"Connected to the server at {host}:{port}")

    # Получение сообщений в отдельном потоке
    _thread.start_new_thread(receive_messages, ())

    # Отправка сообщений серверу
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))

# Основная часть
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
start_client()