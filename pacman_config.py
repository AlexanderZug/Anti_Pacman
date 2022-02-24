import sys
import pygame
from pygame.locals import *
from ghost import Ghost
from game_settings import GameSettings
from ghost_food import Food


class AntiPacmanConfig:
    def __init__(self):
        self.window_surface = pygame.display.set_mode((GameSettings().window_width, GameSettings().window_height))
        self.main_clock = pygame.time.Clock()
        self.music_playing = True
        self.ghost = Ghost(self.window_surface)
        self.food = Food(self.window_surface, self.ghost.player)

    def set_pygame_events_config(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            self.ghost.move_keydown(event)
            self.music_bg_stop(event)
            self.escape_exit(event)
        self.main_clock.tick(GameSettings().FPS)

    def blit_unit(self, img_unit, unit):
        self.window_surface.blit(img_unit, unit)

    def window_update(self):
        self.window_surface.fill(GameSettings().bg_colour)
        self.ghost.move_it_speed()
        self.blit_unit(self.ghost.player_img_stretched, self.ghost.player)
        self.food.check_collisions()
        self.food.food_update()
        pygame.display.update()

    def music_bg_stop(self, event):
        if event.type == KEYUP and event.key == K_m:
            if self.music_playing:
                pygame.mixer.music.stop()
            else:
                pygame.mixer.music.play(-1, 0.0)
            self.music_playing = not self.music_playing

    def music_config_bg(self):
        pygame.mixer.music.load('games_music/background.mp3')
        pygame.mixer.music.play(-1, 0.0)
        pygame.mixer.music.set_volume(0.09)

    def escape_exit(self, event):
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()