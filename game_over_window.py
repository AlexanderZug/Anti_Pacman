import sys
import pygame
from pygame.locals import *

from game_settings import GameSettings


class GameStartAndOver:
    def __init__(self, window_surface):
        self.window_surface = window_surface
        self.player = pygame.Rect(15, 520, 40, 40)
        self.player_img = pygame.image.load('games_photos/ghost.png')
        self.player_img_stretched = pygame.transform.scale(self.player_img, (40, 40))

    def wait_for_gamer_query(self):
        self.start_music()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    GameSettings().terminate()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        GameSettings().terminate()
                    return

    def blit_start_photo(self):
        self.window_surface.blit(self.player_img_stretched, self.player)

    def titel_lbl(self):
        titel_text = GameSettings().start_font.render("AntiPacman", True, GameSettings().start_color)
        titel_rect = titel_text.get_rect()
        titel_rect.center = (300, 280)
        self.window_surface.blit(titel_text, titel_rect)
        press_key_text = GameSettings().basic_font.render("Press something to start", True, GameSettings().text_colour)
        press_key_rect = press_key_text.get_rect()
        press_key_rect.center = (300, 400)
        self.window_surface.blit(press_key_text, press_key_rect)

    def start_music(self):
        pygame.mixer.music.load('games_music/start_song.mp3')
        pygame.mixer.music.play(-1, 0.0)
        pygame.mixer.music.set_volume(0.09)




