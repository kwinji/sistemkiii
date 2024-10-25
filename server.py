import socket
import _thread


# Функция для обработки каждого клиента
def handle_client(client_socket, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"[{addr}] {message}")
                broadcast(message, client_socket)
            else:
                break
        except:
            break

    print(f"[DISCONNECTED] {addr} disconnected.")
    clients.remove(client_socket)
    client_socket.close()


# Функция для рассылки сообщений всем клиентам, кроме отправителя
def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                clients.remove(client)


# Настройка сервера
def start_server():
    server_socket.listen(5)
    print(f"[LISTENING] Server is listening on {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        clients.append(client_socket)
        _thread.start_new_thread(handle_client, (client_socket, addr))


# Основная часть
host = socket.gethostname()  # Локальный хост
port = 12345  # Порт



server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))

clients = []

print("[STARTING] Server is starting...")
start_server()