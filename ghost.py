import random
import pygame
from pygame.locals import *
from game_settings import GameSettings


class Ghost:
    def __init__(self, window_surface):
        self.window_surface = window_surface
        self.player = pygame.Rect(15, 520, 40, 40)
        self.player_img = pygame.image.load('games_photos/ghost.png')
        self.player_img_stretched = pygame.transform.scale(self.player_img, (40, 40))
        self.jump_sound = pygame.mixer.Sound('games_music/jump.wav')
        self.move_left = self.move_right = self.move_up = self.move_down = False
        self.move_speed = 1

    def speed_increase(self):
        self.move_speed += 0.5

    def move_keydown(self, event):
        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == K_a:
                self.move_right = False
                self.move_left = True
            if event.key == K_RIGHT or event.key == K_d:
                self.move_left = False
                self.move_right = True
            if event.key == K_DOWN or event.key == K_s:
                self.move_up = False
                self.move_down = True
            if event.key == K_UP or event.key == K_w:
                self.move_down = False
                self.move_up = True
        self.move_keyup(event)

    def move_keyup(self, event):
        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_a:
                self.move_left = False
            if event.key == K_RIGHT or event.key == K_d:
                self.move_right = False
            if event.key == K_DOWN or event.key == K_s:
                self.move_down = False
            if event.key == K_UP or event.key == K_w:
                self.move_up = False
            if event.key == K_SPACE:
                self.player.top = random.randint(0, GameSettings().window_height - self.player.height)
                self.player.left = random.randint(0, GameSettings().window_width - self.player.width)
                self.jump_sound.play()

    def move_it_speed(self):
        if self.move_down and self.player.bottom < GameSettings().window_height:
            self.player.bottom += self.move_speed
        if self.move_up and self.player.top > 0:
            self.player.top -= self.move_speed
        if self.move_left and self.player.left > 0.5:
            self.player.left -= self.move_speed
        if self.move_right and self.player.right < GameSettings().window_width:
            self.player.right += self.move_speed

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
            cls.instance.__init__(*args, **kwargs)
        return cls.instance