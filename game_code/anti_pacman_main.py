import pygame
from pacman_config import AntiPacmanConfig


class AntiPacman:
    """Класс для запуска программы, создает объект класса AntiPacmanConfig, где реализована основная логика программы"""
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Anti-Pacman')
        self.config = AntiPacmanConfig()
        self.config.music_config_bg() # Вызов фоновой музыки игры

    def run_game(self):
        """Метод, запускающий игровой цикл и отрисовывающий события"""
        while True:
            self.config.set_pygame_events_config()
            self.config.window_update()


if __name__ == '__main__':
    AntiPacman().run_game()