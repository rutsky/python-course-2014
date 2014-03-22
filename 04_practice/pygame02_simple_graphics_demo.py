# -*- encoding: utf-8 -*-
#
# Рисование
#
# Основано на примерах Simpson College Computer Science <http://cs.simpson.edu>

import pygame
from math import pi

# Определим константы для цветов (модель RGB)
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)


def main_impl():
    # Инициализируем экран для рисования
    size = (400, 500)
    screen = pygame.display.set_mode(size)

    # Установим заголовок окна
    pygame.display.set_caption("My Game 2")

    # Флаг: стоит ли завершить игру
    done = False

    # Создадим таймер для ограничения числа FPS
    clock = pygame.time.Clock()

    # ------- главный цикл приложения
    while not done:
        # Обработаем события (ввод с клавиатуры, мышь и т.п.)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # пользователь нажал кнопку закрытия окна
                done = True # завершить главный цикл на следующей итерации

        # ------- отрисовка
        # Закрасим экран белым цветом
        screen.fill(white)

        # Рисуем зелёную линию от (0, 0) до (100, 100) толщиной 5 пикселей
        pygame.draw.line(screen, green, (0,0), (100, 100), 5)

        # Рисуем несколько красных линий в цикле
        for y_offset in range(0, 100, 10):
            pygame.draw.line(screen, red,
                (0, 10 + y_offset), (100, 110 + y_offset), 5)

        # Выбираем шрифт для рисования текста: по умолчанию, высотой 25 пикселей
        font = pygame.font.Font(None, 25)

        # Создаём изображение с текстом. True — использовать сглаживание
        text = font.render("My text + текст на русском", True, black)

        # Рисуем изображение с текстом на экран в позиции (250, 250).
        screen.blit(text, (150, 250))

        # Рисуем прямоугольник
        pygame.draw.rect(screen, black, (20, 20, 250, 100), 2)

        # Рисуем эллипс, заданный описывающим прямоугольником
        pygame.draw.ellipse(screen, black, [20, 20, 250, 100], 2)

        # Рисуем дуги.
        pygame.draw.arc(screen, black, (20, 220, 250, 200),
                     0,     pi / 2, 2)
        pygame.draw.arc(screen, green, (20, 220, 250, 200),
                pi / 2,         pi, 2)
        pygame.draw.arc(screen, blue,  (20, 220, 250, 200),
                    pi, 3 * pi / 2, 2)
        pygame.draw.arc(screen, red,   (20, 220, 250, 200),
            3 * pi / 2,     2 * pi, 2)

        # Рисуем полигон (треугольник).
        pygame.draw.polygon(screen,black, [(100, 100), (0, 200), (200, 200)], 5)

        # ------- конец отрисовки

        # Ограничиваем частоту обновления экрана 20 кадрами в секунду
        clock.tick(20)

        # Показываем на экран только что нарисованный кадр
        pygame.display.flip()
    

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
