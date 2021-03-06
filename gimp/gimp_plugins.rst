Написание плагинов для GIMP на Python
=====================================

GIMP (http://www.gimp.org/) — растровый графический редактор с открытым
исходным кодом.

Ссылки на документацию.

На русском языке:

* Общая информация о скриптовании в GIMP:
  http://docs.gimp.org/ru/gimp-scripting.html

* Туториалы:
  
  * http://www.ibm.com/developerworks/ru/library/os-autogimp/
  * http://digilinux.ru/2006/06/02/gimp-python-intro/

На английском языке:

* Довольно подробная справка о скриптовании на Python:
  http://www.gimp.org/docs/python/pygimp.html

* Туториалы и материалы по разработке плагинов (в том числе и на Python):
  http://gimpbook.com/scripting/

* Туториал и документация по разработке плагинов на Си (более полная, чем
  справка о написании плагинов на Python):

  * http://developer.gimp.org/plug-ins.html
  * http://www.gimp.org/docs/plug-in/plug-in.html

Примеры плагинов на Python, входящих в поставку GIMP 2.8:

* https://git.gnome.org/browse/gimp/tree/plug-ins/pygimp/plug-ins?h=gimp-2-8

Большое количество готовых плагинов (в том числе написанных на Python) можно
найти в реестре плагинов: http://registry.gimp.org/

Плагины в GIMP представляют собой внешние исполняемые модули или скрипты.
Плагины можно разрабатывать на C, используя библиотеку libgimp для
взаимодействия с GIMP, или на одном из скриптовых языков.

На данный момент GIMP поставляется с поддержкой скриптов на собственном 
диалекте Scheme.
При установке GIMP есть возможность установить поддержку скриптов на
Python 2.7, этой возможностью следует воспользоваться.
Существует возможность написания плагинов на Perl, C++, C#, Ruby, но
плагины для поддержки этих языков плохо поддерживаются и требуют дополнительных
шагов для установки.

С помощью плагинов можно реализовывать новую функциональность (например,
фильтры для изображений, поддержку импорта/экспорта в различные форматы),
и автоматизировать рутинную работу (например, применить одинаковую
последовательность операций над группой изображений).

Для взаимодействия GIMP и плагинов используется специальная база данных
процедур (PDB, Procedural database).

В PDB плагины и GIMP регистрируют высокоуровневые функции.
Через PDB эти функции можно вызывать и получать результат выполнения.

Функции в PDB строго типизированы специфичными для GIMP типами: аргументы
функции фиксируются при её регистрации, и имеют типы вроде "изображение",
"целое число", "поверхность для рисования".
Опционально, функции могут привязываться к какому-то пункту меню, например,
добавить пункт в меню Filters.

Для ряда встроенных в GIMP типов есть готовые диалоги, позволяющие запросить
у пользователя тот или иной параметр (например, выбрать цвет, выбрать
число-параметр из заданного диапазона).

Архитектура плагинов в GIMP
---------------------------

Каждый плагин должен предоставить как минимум две функции через специальный API
для корректной работы:

* query — запрос у плагина списка процедур, для регистрации в PDB.

* run — запрос на выполнение одной из зарегистрированных в query процедур PDB.

При запуске GIMP опрашивает все новые или изменившиеся плагины из директорий с
плагинами (Edit -> Preferences -> Folders -> Plug-ins).
Каждому плагину предоставляется возможность зарегистрировать одну или несколько
функций в PDB и добавить новые пункты меню.

Функции PDB делятся на следующие категории:

* ``<Image>`` — функции для обработки текущего изображения. Например,
  фильтры.

* ``<Load>`` — функции для загрузки изображений из файлов.

* ``<Save>`` — функции для сохранения изображений в файлы.

* ``<Toolbox>`` — функции без специального назначения. Могут вызываться
  другими плагинами. Например, функции для преобразования изображений из
  одного формата в другой.

Разные категории функций имеют разные наборы обязательных аргументов, например,
``<Load>`` функции принимают имя файла для загрузки, а ``<Image>`` функции
принимают текущее изображение и текущую поверхность для рисования.

Во время работы GIMP может вызвать функцию из плагина в результате одного из
событий:

* Попытка открыть файл с изображением, для которого зарегистрирована функция 
  загрузки (``<Load>``).

* Попытка сохранить файл с изображением в формате, для которого
  зарегистрирована специальная функция сохранения (``<Save>``).

* Выбран пункт меню, ассоциированный с функцией PDB.

* Какой-то плагин вызвал функцию через PDB.

При вызове PDB функции, зарегистрированной из Python скрипта, GIMP выполнит
python скрипт плагина так, что в нём будет вызвана соответствующая функция
на python (указанная при регистрации в PDB).
Таким образом, при успешной регистрации плагина, плагин можно редактировать
и при каждом следующем запуске функции из него будет выполнена последняя
версия — нет необходимости перезапускать GIMP.

В GIMP доступна встроенная консоль Python с похожим окружением на то, что
используется внутри плагинов на Python.
Её можно запустить из Filters -> Python-Fu -> Console.

В окне с консолью можно запустить браузер зарегистрированных функций
(кнопка ``Browse...``).
