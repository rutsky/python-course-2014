#include <SDL/SDL.h>

int main( int argc, char * args[] )
{
  SDL_Surface * screen = NULL;

  // Инициализация библиотеки SDL
  SDL_Init(SDL_INIT_EVERYTHING);

  // Создаём окно для рисования (или полный экран)
  screen = SDL_SetVideoMode(640, 480, 32, SDL_SWSURFACE);

  // Пауза 4 секунды
  SDL_Delay(4000);

  // Деинициализация SDL
  SDL_Quit();

  return 0;
}
