
import pygame
from pygame.locals import *

from game_settings import GameSettings


class GameStartOverWindows:
    def __init__(self, window_surface):
        self.window_surface = window_surface
        self.player = pygame.Rect(15, 520, 40, 40)
        self.player_img = pygame.image.load('games_photos/ghost.png')
        self.player_img_stretched = pygame.transform.scale(self.player_img, (40, 40))
        self.over_sound = pygame.mixer.Sound('games_music/game_over.wav')

    def wait_for_gamer_query_start(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    GameSettings().terminate()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        GameSettings().terminate()
                    return

    def titel_lbl(self):
        titel_text = GameSettings().start_font.render("AntiPacman", True, GameSettings().start_color)
        titel_rect = titel_text.get_rect()
        titel_rect.center = (300, 280)
        self.window_surface.blit(titel_text, titel_rect)
        press_key_text = GameSettings().basic_font.render("Press something to start", True, GameSettings().text_colour)
        press_key_rect = press_key_text.get_rect()
        press_key_rect.center = (300, 400)
        self.window_surface.blit(press_key_text, press_key_rect)
        self.window_surface.blit(self.player_img_stretched, self.player)

    def game_over_titel(self, score, lvl):
        game_over_titel_text = GameSettings().start_font.render("Game Over", True, GameSettings().start_color)
        game_over_titel_rect = game_over_titel_text.get_rect()
        game_over_titel_rect.center = (300, 280)
        self.window_surface.blit(game_over_titel_text, game_over_titel_rect)
        score_text = GameSettings().basic_font.render(f"Score: {score}", True, GameSettings().text_colour)
        score_text_rect = score_text.get_rect()
        score_text_rect.center = (200, 400)
        self.window_surface.blit(score_text, score_text_rect)
        lvl_text = GameSettings().basic_font.render(f"Level: {lvl}", True, GameSettings().text_colour)
        lvl_text_rect = lvl_text.get_rect()
        lvl_text_rect.center = (400, 400)
        self.window_surface.blit(lvl_text, lvl_text_rect)
        self.over_sound.play()

    @staticmethod
    def start_music():
        pygame.mixer.music.load('games_music/start_song.mp3')
        pygame.mixer.music.play(-1, 0.0)
        pygame.mixer.music.set_volume(0.09)

    @staticmethod
    def stop_start_music():
        pygame.mixer.music.stop()




