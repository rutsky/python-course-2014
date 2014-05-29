
.. Язык программирования Python
   Лекция № 10.

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

Лекция № 10

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

* IPython

* Математические библиотеки

* Sage


IPython
=======

* **IPython** (http://ipython.org/) — изначально, продвинутая командная строка для интерактивного выполнения Python

  * автодополнение (интроспекция), вызов системных команд, встроенная справка, удобный вывод контейнеров

* Выросла до клиент-серверной системы, не привязанной к Python

  * имеет веб-интерфейс, средства для параллельной обработки данных (включая работу на кластерах), интеграцию с графическими тулкитами


Пример интерактивной сессии
===========================

* Установка::

    pip install ipython

  Для различных фич потребуются различные пакеты (`PyQt`, `matplotlib`)

  Можно поставить готовую сборку (рекомендую)

* Документация: http://ipython.org/ipython-doc/stable/interactive/index.html


matplotlib
==========

* **matplotlib** (http://matplotlib.org/) — популярная библиотека для визуализации данных

  * Визуализация данных, графики, диаграммы

  * Многое в синтаксисе взято из средств визуализации графиков в MATLAB

* Примеры: http://matplotlib.org/examples/index.html

* Галерея примеров: http://matplotlib.org/gallery.html

numpy, scipy
============

* **numpy** (http://www.numpy.org/) — библиотека для работы с многомерными массивами данных

  * вектора, матрицы, пиксели изображений

  * данные обрабатываются **векторно**, используя специальные инструкции процессора — скорость работы сопоставима со скоростью работы программ на Си

* **scipy** (http://www.scipy.org/) — фреймворк, интегрирующий в себя ipython, matplotlib, numpy и др., плюс дополнительные алгоритмы обработки данных

* Туториал: http://wiki.scipy.org/Tentative_NumPy_Tutorial

* Примеры: http://wiki.scipy.org/Numpy_Example_List

sympy
=====

* **sympy** (http://sympy.org) — библиотека для *символьных* вычислений

* **Символьные вычисления** — преобразования и работа с математическими равенствами и формулами как с последовательностью символов

* Туториал: http://docs.sympy.org/latest/tutorial/index.html

IPython notebook
================

* А что если сделать текстовый редактор, куда можно писать не только текст, но и код, который будет выполняться (вычислять, рисовать графики и т.п.)?

  * IPython Notebook

  * Цель: удобное создание воспроизводимых научных работ

* Документация: http://ipython.org/ipython-doc/stable/notebook/index.html

* Примеры: http://nbviewer.ipython.org/github/ipython/ipython/tree/1.x/examples/notebooks/

Sage
====

* Sage (http://sagemath.org/index.html) — математический пакет, включающий в себя NumPy, SciPy, matplotlib, Sympy, Maxima, GAP, FLINT, R и многие другие библиотеки

* Имеет веб-интерфейс, как и IPython notebook: Sage Notebook (http://www.sagenb.org/)

* Если IPython — это стандартный Python, с удобным интерфейсом к математическим библиотекам, то Sage — это *модицифированный* Python, ориентированный на математические операции

* Документация: http://sagemath.org/tour.html

* Примеры: http://wiki.sagemath.org/pics

SageMathCloud
=============

* **SageMathCloud** (https://cloud.sagemath.com/) — продвинутая версия Sage Notebook (пока в стадии открытой беты)

  * улучшенный веб-интерфейс

  * поддержка IPython notebook, редактирования LaTeX, распределённых вычислений на кластерах

