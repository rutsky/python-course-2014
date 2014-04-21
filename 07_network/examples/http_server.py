import http.server
import socketserver

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write("""\
            <!DOCTYPE html>
            <html>
            <head>
              <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
              <title>Заголовок окна</title>
            </head>
            <body>
              <h1>Заголовок страницы</h1>
              <p>Параграф с <b>жирным</b> и <i>наклонным</i> текстом.</p>
            </body>
            </html>
            """.encode('utf-8'))

if __name__ == "__main__":
    server = http.server.HTTPServer(('localhost', 8080), MyHandler)
    print('Started http server')
    server.serve_forever()
