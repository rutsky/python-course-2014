# -*- encoding: utf-8 -*-
#
# Обработка мыши
#
# Основано на примерах Simpson College Computer Science <http://cs.simpson.edu>

import pygame
import math

# Определим константы для цветов (модель RGB)
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
dkgreen = (0, 100, 0)
purple = (0xBF, 0x0F, 0xB5)
brown = (0x55, 0x33, 0x00)


def draw_background(screen):
    """Отрисовка заднего фона"""

    # Заполняем белым цветом
    screen.fill(white)


def draw_item(screen, x_float, y_float):
    # Округлим позицию, т.к. функции рисования принимают int
    x = round(x_float)
    y = round(y_float)

    pygame.draw.rect(screen, green, [0 + x, 0 + y, 30, 10], 0)
    pygame.draw.circle(screen, black, [15 + x, 5 + y], 7, 0)


def main_impl():
    # Инициализируем экран для рисования
    size = (640, 480)
    screen = pygame.display.set_mode(size)

    clock = pygame.time.Clock()

    # Флаг: стоит ли завершить игру
    done = False

    # ------- главный цикл приложения
    while not done:
        # Обработаем события (ввод с клавиатуры, мышь и т.п.)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # пользователь нажал кнопку закрытия окна
                done = True  # завершить главный цикл на следующей итерации

        # Получаем текущую позицию мыши
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Рисуем задний фон
        draw_background(screen)

        # Рисуем объект
        draw_item(screen, mouse_x, mouse_y)

        # Показываем на экран только что нарисованный кадр
        pygame.display.flip()

        # Ограничиваем частоту обновления экрана 40 кадрами в секунду
        clock.tick(40)


def main():
    # Инициализируем библиотеку PyGame.
    pygame.init()

    try:
        main_impl()
    finally:
        # Всегда деинициализируем библиотеку PyGame, даже в случае падения.
        pygame.quit()


if __name__ == "__main__":
    main()
