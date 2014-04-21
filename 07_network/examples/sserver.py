import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    На каждое соединение клиента будет создан экземпляр данного класса
    и вызван метод handle().
    """

    def handle(self):
        # self.request это сокет, соединённый с клиентом
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(repr(self.client_address)))
        print(self.data)
        # Отправим клиенту те же данные, что он прислал, только в верхнем
        # регистре
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Создаём сервер, который будет слушать (HOST, PORT)
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Запускаем сервер. Он будет работать "вечно" (пока не прервут по Ctrl+C)
    server.serve_forever()
