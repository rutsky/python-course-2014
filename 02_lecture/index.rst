
.. Язык программирования Python
   Лекция № 2.

.. role:: python(code)
   :language: python

.. TODO : в заголовке документа должен быть Python

=====================
Язык программирования
=====================

.. rst-class:: python-logo
.. figure:: ../common/images/python-logo-generic.svg
   :align: center

.. rst-class:: center-text

Лекция № 2

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

* Повторение

* 

* Практика


Повторение
==========


Модули
======

* Программы на Python пишутся внутри ``*.py`` файлов — **модулей**

* Модули можно *выполнять* (``python.exe hello.py``):

  .. literalinclude:: examples/hello.py

* Объекты из модулей можно *использовать* в других модулях (или в интерактивном
  режиме) с помощью команды ``import``:

  .. literalinclude:: examples/import.pycon


.. rst-class:: smaller2

Стандартная библиотека (1/2)
============================

* Стандартная библиотека Python состоит из большого числа модулей:
  http://docs.python.org/3/library/index.html

  - Работа со строками
  - Работа с двоичными данными
  - Структуры данных
  - Математические функции и типы
  - Объекты для функционального программирования
  - Работа с файлами и директориями
  - Сериализация и сохранение данных, БД
  - Сжатие данных и работа с архивами
  - Работа с файлами определённых типов
  - Криптографические функции
  - Работа с ОС
  - Параллельное выполнение кода
  - ...

.. rst-class:: smaller2

Стандартная библиотека (2/2)
============================

* продолжение:

  - Межпроцессорное взаимодействие
  - Работа с типами Internet
  - Работа с HTML/XML
  - Интернет протоколы
  - Мультимедиа
  - Интернационализация
  - Фреймворки для программ
  - Графический интерфейс с помощью Tk
  - Средства для разработки
  - Средства отладки и профилирования


.. rst-class:: smaller

Модуль :py:mod:`random`
=======================

.. literalinclude:: examples/random.pycon


.. rst-class:: smaller

Способы импортирования
======================

.. literalinclude:: examples/import_as.pycon


Модуль :py:mod:`builtins`
=========================

.. literalinclude:: examples/builtins.pycon


.. rst-class:: smaller

Пакеты
======

Модули можно объединять в пакеты::

  sound/           Пакет верхнего уровня
      __init__.py      Инициализация пакета работы со звуком (sound)
      formats/         Подпакет для конвертирования форматов файлов
          __init__.py
          wavread.py       (чтение wav)
          wavwrite.py      (запись wav)
      effects/         Подпакет для звуковых эффектов
          __init__.py
          echo.py          (эхо)
          surround.py      (фон)
          reverse.py       (обращение)

Использование::

  # Импортируем модуль sound/effects/echo.py
  import sound.effects.echo
  sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)

или::

  from sound.effects import echo
  echo.echofilter(input, output, delay=0.7, atten=4)


.. rst-class:: smaller

Файл ``__init__.py``
====================

* Пакет — директория, содержащая модули и/или пакеты

* Модуль можно превратить в пакет (и наоборот):

  - ``sum`` как модуль:

    ``sum.py``::

      def my_sum(a, b):
          return a + b

  - ``sum`` как пакет:

    ``sum/__init__.py``::

      def my_sum(a, b):
          return a + b

* Использование одинаковое::

    >>> import sum
    >>> sum.my_sum(10, 20)
    30
    >>>
   

.. rst-class:: smaller

Функция :py:func:`dir`
======================

.. literalinclude:: examples/dir.pycon
   :linenos:

