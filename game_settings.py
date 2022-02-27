import pygame


class GameSettings:
    def __init__(self):
        self.window_width = 600
        self.window_height = 600
        self.FPS = 90
        self.basic_font = pygame.font.SysFont('aquakana', 20)
        self.start_font = pygame.font.SysFont('gabriola', 90)
        self.bg_colour = (0, 0, 0)
        self.text_colour = (255, 255, 255)
        self.start_color = (255, 0, 0)
