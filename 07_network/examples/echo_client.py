# Echo client program
import socket

HOST = 'localhost'        # Имя сервера, к которому будем коннектиться
PORT = 50007              # Номер порта на сервере
# Создаём интернет-сокет для использования по протоколу TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Соединяемся с сервером
s.connect((HOST, PORT))
# Посылаем серверу байтовую строку
s.sendall(b'Hello, world')
# Принимаем от сервера данные
data = s.recv(1024)
# Закрываем соединение
s.close()
print('Received', repr(data))
