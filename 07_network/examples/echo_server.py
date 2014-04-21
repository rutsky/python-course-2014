# Echo server program
import socket

HOST = ''                 # Слушать все интерфейсы
PORT = 50007              # Порт, который необходимо слушать
# Создаём интернет-сокет для использования по протоколу TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Будем слушать все интерфейсы на порту PORT
s.bind((HOST, PORT))
# Переводим сокет в режим ожидания соединений
s.listen(1)
# Ждём соединения от клиента
conn, addr = s.accept()
print('Connected by', addr)
while True:
    # Считываем данные от клиента
    data = conn.recv(1024)
    if not data:
        break
    # Пишем считанные данные обратно клиенту
    conn.sendall(data)
# Закрываем соединение
conn.close()
