Лекция 1. Введение в язык программирования Python
=================================================

Установка Python
----------------

1. Скачиваем дистрибутив Python 3.3 с официального сайта http://python.org

   * Последняя версия на данный момент 3.3.4:
     http://python.org/download/releases/3.3.4/

   * Для Windows ищите на странице ссылку
     "``Windows X86 MSI Installer (3.3.4)``" (или "``X86-64``")

2. Устанавливаем в директорию по умолчанию (``C:\Python33``)

Интепретатор: "``C:\Python33\python.exe``"


Установка и настройка PyCharm
-----------------------------

1. Скачиваем дистрибутив PyCharm Community Edition с официального сайта
   http://www.jetbrains.com

   * http://www.jetbrains.com/pycharm/download/

   * Community Edition — бесплатный и под свободной лиценцией

2. Устанавливаем

   * при установке можно выбрать цветовую схему и вариант раскладки — можно
     выбрать всё по умолчанию

3. Запускаем

4. Окно "``Welcome to PyCharm Community Edition``"

   * ``Open Directory``

     Выбираем директорию, где будем хранить наши Python скрипты

     Например, ``C:\python-scripts\``

     Потом мы научимся создавать и настраивать проекты, пока просто проект-директория.

     Созданный проект будет называться по имени директории (``python-scripts``)

3. Настройка используемого в PyCharm интерпретатора

   1. ``File -> Settings -> Project Interpreter -> Python Interpreters``

   2. Нажимаем "``+``", выбираем "``Local...``"

   3. Выбираем ``C:\Python33\python.exe``, ``Ok``.

   4. "``Do you want to set this interpreter as Project Interpreter?``" — "``Yes``"

   5. "``Ok``" в диалоге

4. Создание Python-cкрипта

   1. Кликните правой кнопкой мыши на имени проекта ``-> New -> Python File``

   2. Введите имя, например, ``program.py``

5. Отредактируйте скрипт

6. Запуск скрипта ``Run -> Run...``, в диалоге выбора файлов выберите текущий
   скрипт (``program.py``)

   Вывод скрипта и код выхода появится в панели снизу.

7. Запуск интерпретатора Python (интерактивная сессия)

   * ``Tools -> Run Python Console...``

tttt
----

.. literalinclude:: ../01_introduction/examples/07_strings_indexing.pycon
