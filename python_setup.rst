Установка Python
----------------

В Windows:

1. Загрузите дистрибутив Python 3.3 с официального сайта http://python.org.

   Последняя версия на данный момент 3.3.4:
   http://python.org/download/releases/3.3.4/.

   Ищите на странице ссылку
   ``Windows X86 MSI Installer (3.3.4)`` (или "``X86-64``").

2. Установите в директорию по умолчанию (``C:\Python33``).

Интепретатор: ``C:\Python33\python.exe``


Запуск Python
-------------

Для интерактивной сессии запустите ``python.exe`` из директории установки::

    C:\>C:\Python33\python.exe
    Python 3.3.4 (v3.3.4:7ff62415e426, Feb 10 2014, 18:12:08) [MSC v.1600 32 bit (Intel)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>> print("Hello, world!")
    Hello!
    >>>

Для запуска скрипта на Python сохранённого в файле ``hello.py``::

    C:\>C:\Python33\python.exe hello.py
    Hello, world!
    C:\>

Содержимое ``hello.py``::

    print("Hello, world!")


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


Шаблон программы на Python
--------------------------

   .. code-block:: python
   
      # Шаблон программы на Python
      #
      # Это комментарий. Любую программу стоит начинать с описания того,
      # для чего она предназначена.
      
      # Импортируем необходимые модули
      import sys
      
      def main():
          """Main program function"""
      
          # sys.argv содержит список аргументов командной строки.
          # sys.argv[0] хранит имя запущенного скрипта.
      
          if len(sys.argv) == 1:
              print("Ошибка! Слишком мало аргументов!")
              sys.exit(1)
      
          else:
              print("Программа", sys.argv[0], "была запущена с аргументами:")
              for arg in sys.argv[1:]:
                  print(arg)
      
      if __name__ == "__main__":
          # Если скрипт запущен как "python.exe template.py",
          # то это условие будет выполнено и будет вызвана main().
          # Впоследствии можно будет написать тесты, которые будут
          # импортировать этот модуль и вызывать функции из него.
          main()