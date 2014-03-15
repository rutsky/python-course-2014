# -*- encoding: utf-8 -*-
#
# Отрисовка изображений
#
# Основано на примерах Simpson College Computer Science <http://cs.simpson.edu>

import pygame

# Определим константы для цветов (модель RGB)
white = (255, 255, 255)
black = (0, 0, 0)


def main_impl():
    # Инициализируем экран для рисования
    size = (800, 600)
    screen = pygame.display.set_mode(size)

    # Создадим поверхность для рисования
    background = pygame.Surface(screen.get_size())

    # Заполним поверхность черным цветом
    background.fill(black)

    clock = pygame.time.Clock()

    # Загружаем звук из файла
    click_sound = pygame.mixer.Sound("click.wav")

    # Положения заднего фона
    background_position = [0, 0]

    # Загрузим изображение фона
    background_image = pygame.image.load("saturn_family1.jpg").convert()

    # Загрузим изображение курсора
    player_image = pygame.image.load("player.png").convert()
    player_image.set_colorkey(white)  # зададим цвет прозрачности

    # Флаг: стоит ли завершить игру
    done = False

    # ------- главный цикл приложения
    while not done:
        # Обработаем события (ввод с клавиатуры, мышь и т.п.)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # пользователь нажал кнопку закрытия окна
                done = True  # завершить главный цикл на следующей итерации

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Если нажата кнопка мыши — проиграть звук
                click_sound.play()

        # Копируем фоновое изображение из поверхности на экран в координаты
        # background_position
        screen.blit(background_image, background_position)

        # Получаем позицию мышки
        x, y = pygame.mouse.get_pos()

        # Копируем изображение курсора на экран в положение мышки
        screen.blit(player_image, (x, y))

        pygame.display.flip()

        # Ограничиваем частоту обновления экрана 50 кадрами в секунду
        clock.tick(50)


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
