import sys

import pygame

from pygame.locals import *


class GameSettings:
    """
    Класс с базовыми настройками ширины и высоты игрового поля, цветами,
    текстом и FPS; содержит статические методы
    для выхода и для запуска игрового цикла,
    ожидающего нажатия клавиши пользователем
    - применяется в стартовом и финальном окне.
    """

    def __init__(self):
        self.window_width = 600
        self.window_height = 600
        self.FPS = 90
        self.basic_font = pygame.font.SysFont('aquakana', 20)
        self.start_font = pygame.font.SysFont('gabriola', 90)
        self.bg_colour = (0, 0, 0)
        self.bg_img = pygame.image.load('games_photos/bg_img.png')
        self.text_colour = (255, 255, 255)
        self.start_color = (255, 0, 0)

    @staticmethod
    def terminate():
        pygame.quit()
        sys.exit()

    @staticmethod
    def wait_for_gamer_query_final():
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    GameSettings().terminate()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        GameSettings().terminate()
                    return
