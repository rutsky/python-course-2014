import pygame

def main():
    # Инициализация библиотеки SDL
    pygame.init()
 
    # Создаём окно для рисования (или полный экран)
    screen = pygame.display.set_mode([640, 480])

    # Пауза 4 секунды
    pygame.time.wait(4000)

    # Деинициализация SDL
    pygame.quit()

if __name__ == "__main__":
    main()
