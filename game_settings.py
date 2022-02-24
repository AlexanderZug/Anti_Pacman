import pygame


class GameSettings:
    def __init__(self):
        self.window_width = 600
        self.window_height = 600
        self.FPS = 90
        self.basic_font = pygame.font.SysFont('aquakana', 48)
        self.bg_colour = (0, 0, 0)