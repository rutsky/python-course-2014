
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

* Модули, области видимости, полезные функции

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

Способы импортирования (1/2)
============================

.. literalinclude:: examples/import_as.pycon


.. rst-class:: smaller2

Способы импортирования (2/2)
============================

.. literalinclude:: examples/import_all.pycon


.. rst-class:: smaller2

Скрытие имён в модулях (1/2)
============================

``from ... import *`` не импортирует имена, начинающиеся с подчеркивания — в
Python принято называть "скрытые" функции и имена с подчеркивания

.. literalinclude:: examples/rndcolors1.py

.. literalinclude:: examples/rndcolors1.pycon

.. literalinclude:: examples/rndcolors2.py

.. literalinclude:: examples/rndcolors2.pycon


.. rst-class:: smaller2

Скрытие имён в модулях (2/2)
============================

Если в модуле объявлена глобальная переменная ``__all__``, то с помощью
``from ... import *`` из этого модуля будут импортироваться только имена, 
перечисленные в списке или кортеже ``__all__``

.. literalinclude:: examples/rndcolors3.py

.. literalinclude:: examples/rndcolors3.pycon



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


.. rst-class:: smaller2

Способы выполнения кода на Python (1/2)
=======================================

Прямые способы:

* Интерактивный режим::

     >>> a = 10

* Запуск модуля::
  
     C:\>C:\Python33\python.exe hello.py
     Hello!
     C:\>

* Выполнение команд, непосредственно переданных интерпретатору::

     C:\>C:\Python33\python.exe -c "a = 10; print(a)"
     10
     C:\>

* Запуск модуля, доступного в текущем дистрибутиве Python::

     C:\>C:\Python33\python.exe -m random
     2000 times random
     0.001 sec, avg 0.500839, stddev 0.287432, min 0.000557505, max 0.999779
     2000 times normalvariate
     0.003 sec, avg 0.0308376, stddev 1.02038, min -3.30629, max 3.85466
     ...
     C:\>


.. rst-class:: smaller2

Способы выполнения кода на Python (2/2)
=======================================

Косвенные способы — при импортировании модулей::

     >>> import random  # В результате этой команды модуль будет интерпретирован
     >>>

``module.py``:

.. literalinclude:: examples/module.py

При прямом способе выполнения команды, вводимые в интерактивном режиме, или из 
интерпретируемого модуля, или из аргументов к ``python.exe -c``, выполняются
в виртуальном модуле с именем ``__main__``::

  C:\>C:\Python33\python.exe module.py
  This module '__name__' variable is: __main__
  C:\>

При интерпретировании модуля в результате импортирования (косвенный способ
выполнения) ``__name__`` будет указывать на имя модуля::

  >>> import module
  This module '__name__' variable is: module


.. rst-class:: smaller2

Отладочный код в библиотеках
============================

* С помощью ``__name__`` можно определить импортирован ли модуль, либо он выполняется
  напрямую

* Типичное использование в библиотеках — при запуске библиотечного модуля
  запускать тесты; ``even.py``:

  .. literalinclude:: examples/even.py
     :linenos:

  .. code-block:: none

     C:\>C:\Python33\python.exe -m even.py
     Traceback (most recent call last):
       File "module_test.py", line 17, in <module>
         _test()
       File "module_test.py", line 13, in _test
         assert is_even(2)
     AssertionError
     C:\>


.. rst-class:: smaller2

Шаблон программы на Python (1/2)
================================

.. literalinclude:: examples/template.py
   :linenos:


.. rst-class:: smaller2

Шаблон программы на Python (2/2)
================================

.. code-block:: none

   C:\>C:\Python33\python.exe template.py

.. literalinclude:: examples/template.out1

.. code-block:: none

   C:\>C:\Python33\python.exe template.py Питон 1 2 3

.. literalinclude:: examples/template.out2


.. rst-class:: smaller2

Модуль :py:mod:`pprint`
=======================

* .. function:: pprint.pprint(object, stream=None, indent=1, width=80, depth=None)

     "pretty-print".
     Выводит на экран текстовое представление объекта с отступами и переносами строк

     То же, что и просто ``print()``, но форматированное

     .. literalinclude:: examples/pprint.pycon

* .. function:: pprint.pformat(object, indent=1, width=80, depth=None)

     Возвращает строку с результатом, вместо печати на экран


.. rst-class:: smaller2

Имена (переменные) в Python
===========================

* В Python имена — это метки, *ссылающиеся* на объекты
  в памяти (*связанные* с объектами, *binded*)

* Чтобы создать новую метку (или переопределить старую) можно использовать:
  
  * команду присваивания::

      a = 30

  * команду опеределения функции (или класса)::

      def my_sum(x, y):
          return x + y

  * команду ``import``::

      import random


.. rst-class:: smaller2

Области видимости
=================

* Код на Python может выполняться:
  
  * непосредственно внутри модуля
  * внутри функции

* Перед выполнением кода внутри модуля или функции, интерпретатор создаёт
  *область видимости* для модуля или функции (далее о.в.)

* Область видимости — это словарь пар:

  * (имя метки, объект)

* При создании новой метки она помещается в словарь текущей области видимости


.. rst-class:: smaller2

Область видимости в модуле
==========================

.. literalinclude:: examples/scopes_module.pycon


.. rst-class:: smaller2

Область видимости в функции
===========================

.. literalinclude:: examples/scopes_func.pycon


.. rst-class:: smaller2

Поиск имён
==========

* Все метки в Python определены в каком-то модуле

* Для блока кода определена глобальная область видимости —
  область видимости модуля, в котором этот блок кода был задан

* Когда в каком-то блоке происходит обращение к метке, интерпретатор смотрит в следующие о.в.:

  * локальную о.в. блока
  * внешние о.в. для текущего блока 
    
    * если, например, функция задана внутри функции

  * глобальную о.в. для текущего блока

    * модуль, в котором блок определён

  * встроенную о.в.
  
    * содержимое модуля :py:mod:`builtins`


.. rst-class:: smaller2

Глобальная область видимости
============================

.. literalinclude:: examples/scopes_global.pycon


.. rst-class:: smaller2

Команда ``global``
==================

.. literalinclude:: examples/scopes_global2.pycon


.. todo nonlocal, содержимое модуля — его глоб. о.в., пример вложенных о.в.

.. rst-class:: smaller2

Функция :py:func:`enumerate`
============================

* ``enumerate(iter, start=0)`` — "пересчитать"

  - ``iter`` — последовательность
  - ``start`` — опциональный начальный индекс
  - возвращает последовательность пар (индекс, элемент ``iter``)

.. literalinclude:: examples/enumerate.pycon


.. rst-class:: smaller2

Функция :py:func:`zip` (1/2)
============================

* ``zip(iter1[, iter2[, ...]])``

  - от англ. «zip» — «застёжка молния» — соединить два списка, как зубцы молнии

  - ``iter*`` — последовательности
  - возвращает последовательность кортежей:
    
    - (первые элементы последовательностей)
    - (вторые эелементы последовательностей)
    - (третьи эелементы последовательностей)
    - ...
  
  - длина результирующей последовательности равна минимальной длине входной последовательности

.. rst-class:: smaller2

Функция :py:func:`zip` (2/2)
============================

.. literalinclude:: examples/zip.pycon


.. rst-class:: smaller2

Функция :py:func:`map` (1/2)
============================

* ``map(func, iter1[, iter2[, ...]])`` — применить ``func`` к каждому элем. посл.

  - ``iter*`` — последовательности аргументов
  - возвращает последовательность:
    
    - func(первые элементы последовательностей)
    - func(вторые эелементы последовательностей)
    - func(третьи эелементы последовательностей)
    - ...
  
  - длина результирующей последовательности равна минимальной длине входной последовательности

.. rst-class:: smaller2

Функция :py:func:`map` (2/2)
============================

.. literalinclude:: examples/map.pycon


.. rst-class:: smaller2

Функция :py:func:`filter`
=========================

* ``filter(func, iter)`` — вернуть последовательность только из тех элементов ``x``, для которых ``func(x)`` истина

  - ``func`` может быть ``None``, эквивалентно ``filter(bool, iter)``

  .. literalinclude:: examples/filter.pycon


.. rst-class:: smaller2

Форматирование строк
====================

Документация: http://docs.python.org/3/library/string.html#formatstrings

.. literalinclude:: examples/str_format.pycon


.. rst-class:: smaller2

Литералы в других системах счисления
====================================

.. literalinclude:: examples/notations.pycon
   :language: python3


Неименованные функции
=====================

* Можно создать неименованную функцию с помощью ``lambda``::

    >>> f = lambda arg1, arg2: arg1**arg2
    >>> f(2, 3)
    8
    >>>

* Это удобно для обработки списков::

    >>> filter(lambda s: len(s) == 3, ['one', 'two', 'three'])
    ['one', 'two']
    >>>

  фильтрует только те элементы, у которых длина 3

  .. code-block:: python3

       >>> map(lambda x: x**3, range(4))
       [0, 1, 8, 27]
       >>>


.. rst-class:: smaller2

List comprehension (1/2)
========================

* List comprehension — способ задания последовательности

  - [выражение for переменная in послед.]
  - [выражение for переменная in послед. if условие]

* В зависимости от скобок генерируются разные типы данных

  - кортеж:
  
    - (выражение for переменная in послед.)

  - множество:

    - {выражение for переменная in послед.}

  - словарь:
  
    - { выражение-ключ : выражение-значение for переменная in посл. }

* Удобно использовать для inline-создания последовательностей


.. rst-class:: smaller2

List comprehension (2/2)
========================

.. literalinclude:: examples/list_comprehension.pycon


Практика
========
