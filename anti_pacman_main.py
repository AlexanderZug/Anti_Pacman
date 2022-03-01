import pygame
from pacman_config import AntiPacmanConfig


class AntiPacman:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Anti-Pacman')
        self.settings = AntiPacmanConfig()
        self.settings.music_config_bg()

    def run_game(self):
        while True:
            self.settings.set_pygame_events_config()
            self.settings.window_update()


if __name__ == '__main__':
    AntiPacman().run_game()
    AntiPacman().recurs()