#!/usr/bin/env python
# encoding: utf-8

import struct

from gimpfu import *


def write_image_by_pixel(f, layer):
    # Медленная версия итерирования по пикселям изображения.
    # Получать цвет каждого пикселя по отдельности — это _очень_ медленно
    # (и на C/C++ тоже).

    for y in range(layer.height):
        for x in range(layer.width):
            # Получаем цвет пикселя (x, y).
            color = layer.get_pixel(x, y)

            # Упаковываем RGB цвета в трёхбайтовую строку
            # "B" — unsigned char
            rgb_str = struct.pack('BBB', color[0], color[1], color[2])

            f.write(rgb_str)

        # Обновим progress bar
        gimp.progress_update(float(y) / layer.height)


def write_image_by_region(f, layer):
    # Оптимизированная версия: чтения пикселей производится построчно.

    for y in range(layer.height):
        # Запросим строку y изображения с помощью региона.
        src_region = layer.get_pixel_rgn(
            # координаты левого верхнего угла региона
            0, y,
            # ширина и высота региона
            layer.width, 1,
            # dirty — изменения в регионе отразятся на изображении
            False,
            # shadow — операции производятся на shadow тайлах
            False)

        # Регион представляет собой блок памяти с пикселями изображения.
        # В Python они отображаются в строки.

        # Из региона можно получить срезы с областями пикселей следующим
        # образом:
        #     src_region[x, y] — строка "rgb" пикселя в (x, y)
        #     src_region[x1:x2, y]
        #     src_region[x, y1:y1]
        #     src_region[x1:x2, y1:y1]

        # Скопируем RGB каналы пикселей изображения в файл.
        r = src_region[0:layer.width, y]
        # r — строка байт компонент цветов пикселей: RGBARGBARGBA...

        #for r, g, b in zip(r[0::4], r[1::4], r[2::4]):
        #    f.write(r + g + b)

        # немного быстрее:
        for x in range(layer.width):
            f.write(r[x * 4:x * 4 + 3])

        gimp.progress_update(float(y) / layer.height)

    # Можно реализовать ещё быстрее, используя тайлы GIMP.


def read_image_by_region(f, layer):
    for y in range(layer.height):
        # Прочитаем строку изображения из файла
        data = f.read(3 * layer.width)

        # Запросим строку изображения для записи в него с помощью региона.
        dst_region = layer.get_pixel_rgn(
            # координаты левого верхнего угла региона
            0, y,
            # ширина и высота региона
            layer.width, 1,
            # dirty — изменения в регионе отразятся на изображении
            True,
            # shadow — операции производятся на shadow тайлах
            False)

        # Запишем прочитанную строку в изображение.
        dst_region[:layer.width, y] = data

        gimp.progress_update(float(y) / layer.height)


def save_gsm(img, drawable, filename, raw_filename):
    # Т.к. придётся немного модифицировать текущее изображения для его
    # сохранения, сделаем его копию.
    image_copy = pdb.gimp_image_duplicate(img)

    # Изображение в GIMP — довольно сложная сущность, состоящая из слоёв,
    # эффектов и т.п. Для сохранения требуется склеить все слои в один видимый.
    # Здесь в плагинах на Си используется gimp_export_image(), но, похоже, она
    # недоступна плагинам на Python, поэтому воспользуемся другой функцией.
    layer = pdb.gimp_image_merge_visible_layers(image_copy, CLIP_TO_IMAGE)

    #assert layer.type == RGB_IMAGE

    # Инициализируем progress bar
    gimp.progress_init("Saving GSM")

    # Откроем файл, куда необходимо сохранить изображение, в бинарном (!)
    # режиме на запись.
    with open(filename, 'wb') as f:
        # Запакуем в заголовок ширину и длину изображения.
        # "<" — использовать порядок байт little-endian,
        # "H" — запаковать как тип unsigned short (2-х байтовое беззнаковое
        # целое).
        # См. <https://docs.python.org/2/library/struct.html>
        header_str = struct.pack('<HH', layer.width, layer.height)
        # Теперь в header_str 4 байта: два байта с шириной изображения и два
        # байта с высотой.

        # Запишем заголовок в файл.
        f.write(header_str)

        # Запишем цвета пикселей.
        #write_image_by_pixel(f, layer)
        write_image_by_region(f, layer)

    # Завершим progress bar.
    pdb.gimp_progress_end()

    # Освободим ресурсы GIMP, выделенные для копия изображения.
    gimp.delete(image_copy)


def load_gsm(filename, raw_filename):
    # Открываем файл на чтение в бинарном (!) режиме.
    with open(filename, 'rb') as f:
        # Читаем первые 4 байта — заголовок
        header_str = f.read(4)

        # Распаковываем заголовок.
        # "<" — использовать порядок байт little-endian,
        # "H" — запаковать как тип unsigned short (2-х байтовое беззнаковое
        # целое).
        # См. <https://docs.python.org/2/library/struct.html>
        width, height = struct.unpack("<HH", header_str)

        # Создадим RGB изображение подходящего размера.
        image = gimp.Image(width, height, RGB)
        image.filename = filename

        # Создадим слой, куда и будут загружено изображение из файла.
        background = gimp.Layer(image, "Background", width, height,
                                RGB_IMAGE, 100, NORMAL_MODE)

        read_image_by_region(f, background)

        # Добавим слой в изображение.
        image.add_layer(background, 1)

    return image


def register_load_handlers():
    # Регистрируем нашу PDB процедуру для загрузки изображения в формате GSM.
    gimp.register_load_handler('file-gsm-load', 'gsm', '')
    #pdb['gimp-register-file-handler-mime']('file-gsm-load', 'image/gsm')


def register_save_handlers():
    # Регистрируем нашу PDB процедуру для сохранения изображения в формате GSM.
    gimp.register_save_handler('file-gsm-save', 'gsm', '')


# Регистрируем процедуры в PDB

register(
    'file-gsm-save', # имя процедуры в PDB
    'save an GSM (.gsm) file', # описание
    'save an GSM (.gsm) file',
    'Vladimir Rutsky', # автор
    'Vladimir Rutsky', # копирайт
    '2014', # год
    'GSM',
    'RGB', # плагин работает только с RGB изображениями (есть ещё RGBA, GRAY...)
    [
        # аргументы процедуры. Формат: (тип, имя, описание, умолчание [, доп.])
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, "drawable", "Input drawable", None),
        (PF_STRING, "filename", "The name of the file", None),
        (PF_STRING, "raw-filename", "The name of the file", None),
    ],
    [], # возвращаемые значения. Формат: (тип, имя, описание)
    save_gsm, # Python-функция, реализующая регистрируемую процедуру
    on_query=register_save_handlers, # доп. функция, вызываемая при опросе
    menu='<Save>'
)

register(
    'file-gsm-load',
    'load an GSM (.ora) file',
    'load an GSM (.ora) file',
    'Vladimir Rutsky',
    'Vladimir Rutsky',
    '2014',
    'GSM',
    None,
    [
        (PF_STRING, 'filename', 'The name of the file to load', None),
        (PF_STRING, 'raw-filename', 'The name entered', None),
    ],
    [(PF_IMAGE, 'image', 'Output image')],
    load_gsm,
    on_query=register_load_handlers,
    menu = "<Load>",
)

# Явно вызываем gimpfu.main(), в которой реализовано взаимодействие с GIMP.
main()
