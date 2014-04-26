# В Python есть реализация WSGI-совместимого сервера
# Также можно использовать модули Apache/Nginx/IIS для запуска WSGI клиентов
from wsgiref.validate import validator
from wsgiref.simple_server import make_server

# "Запускаем" клиента
import wsgi_client

# Получаем из клиента объект application и оборачиваем его в валидатор
validator_app = validator(wsgi_client.application)

# Создаём и запускаем сервер
httpd = make_server('', 8010, validator_app)
print("Listening on port 8010...")
httpd.serve_forever()
