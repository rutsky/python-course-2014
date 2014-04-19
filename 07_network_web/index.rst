
.. Язык программирования Python
   Лекция № 7.

.. role:: python(code)
   :language: python

.. TODO: в заголовке документа должен быть Python

=====================
Язык программирования
=====================

.. rst-class:: python-logo
.. figure:: ../common/images/python-logo-generic.svg
   :align: center

.. rst-class:: center-text

Лекция № 7

.. rst-class:: center-text

Владимир Владимирович Руцкий rutsky.vladimir@gmail.com

.. rst-class:: center-cells
.. list-table::


   * - .. image:: ../common/images/cgsg.png
          :width: 200 px
     - .. image:: ../common/images/logo_jetbrains.svg
     - .. image:: ../common/images/pml30.png
          :width: 200 px


План занятия
============

* Разбор домашнего задания

* Взаимодействие по сети. Сокеты

* Основы WWW: HTML, CSS, JavaScript

* Написание простого веб-сервера


Компьютерные сети
=================

* Сетевой стек. Модель OSI:
  `https://ru.wikipedia.org/wiki/Сетевая\_модель\_OSI
  <https://ru.wikipedia.org/wiki/%D0%A1%D0%B5%D1%82%D0%B5%D0%B2%D0%B0%D1%8F_%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D1%8C_OSI>`_

* Протокол IP: https://ru.wikipedia.org/wiki/IP
  
  Адреса узлов. Подсети. IPv4, IPv6. Маршрутизация. DNS.

* Протокол UDP: https://ru.wikipedia.org/wiki/UDP

  Негарантированная доставка сообщений (дейтаграмм).

* Протокол TCP: https://ru.wikipedia.org/wiki/TCP/IP

  Установление соединения. Плавающее окно передачи данных.

Сокеты
======

* **Сокет** — интерфейс для взаимодействия между процессами

* Существуют *клиентские* и *серверные* сокеты

* Предоставляет файло-подобный интерфейс для передачи данных между клиентом и сервером.

`https://ru.wikipedia.org/wiki/Сокет_(программный_интерфейс)
<https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BA%D0%B5%D1%82_%28%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%BD%D1%8B%D0%B9_%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D1%84%D0%B5%D0%B9%D1%81%29>`_


.. rst-class:: smaller

Сокеты в Python. Сервер
=======================

.. literalinclude:: examples/echo_server.py


.. rst-class:: smaller

Сокеты в Python. Клиент
=======================

.. literalinclude:: examples/echo_client.py

Документация: https://docs.python.org/3/library/socket.html


.. rst-class:: smaller2

SocketServer
============

.. literalinclude:: examples/sserver.py

Документация: https://docs.python.org/3/library/socketserver.html

Чат на Python
=============

.. rst-class:: smaller

Основы web-программирования
===========================

* Браузер

  * HTML (https://ru.wikipedia.org/wiki/HTML)
  
    Самоучитель HTML4: http://htmlbook.ru/samhtml/vvedenie-v-html

    Самоучитель HTML5: http://htmlbook.ru/samhtml5

  * CSS (https://ru.wikipedia.org/wiki/CSS)
  
    Самоучитель: http://htmlbook.ru/samcss
  
  * JavaScript (https://ru.wikipedia.org/wiki/Javascript)

HTML
====

* DOM-модель

* Отображение статического контента

* URL

CSS
===

* Гибкие возможности по управлению *стилями* отображения

JavaScript
==========

* Обработка событий и модификация DOM

Веб-сервер
==========

  * Протокол HTTP (https://ru.wikipedia.org/wiki/HTTP).
  
  * Методы GET, POST, HEAD

  * Формы

.. rst-class:: smaller2

Веб-сервер на Python
====================

.. literalinclude:: examples/http_server.py

http.server
===========

* При исполнении модуля "расшаривает" текущую директорию::

    python -m http.server 8080

Веб-интерфейс для чата
======================
