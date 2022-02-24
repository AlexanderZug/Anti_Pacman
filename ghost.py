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
        self.moveleft = self.moveright = self.moveup = self.movedown = False
        self.movespeed = 1
        # self.move_direction = ['downleft', 'downright', 'upleft', 'upright']
        # # self.DOWNLEFT = 'downleft'
        # # self.DOWNRIGHT = 'downright'
        # # self.UPLEFT = 'upleft'
        # # self.UPRIGHT = 'upright'

    def move_keydown(self, event):
        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == K_a:
                self.moveright = False
                self.moveleft = True
            if event.key == K_RIGHT or event.key == K_d:
                self.moveleft = False
                self.moveright = True
            if event.key == K_DOWN or event.key == K_s:
                self.moveup = False
                self.movedown = True
            if event.key == K_UP or event.key == K_w:
                self.movedown = False
                self.moveup = True
        self.move_keyup(event)

    def move_keyup(self, event):
        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_a:
                self.moveleft = False
            if event.key == K_RIGHT or event.key == K_d:
                self.moveright = False
            if event.key == K_DOWN or event.key == K_s:
                self.movedown = False
            if event.key == K_UP or event.key == K_w:
                self.moveup = False
            if event.key == K_SPACE:
                self.player.top = random.randint(0, GameSettings().window_height - self.player.height)
                self.player.left = random.randint(0, GameSettings().window_width - self.player.width)
                self.jump_sound.play()

    def move_it_speed(self):
        if self.movedown and self.player.bottom < GameSettings().window_height:
            self.player.bottom += self.movespeed
        if self.moveup and self.player.top > 0:
            self.player.top -= self.movespeed
        if self.moveleft and self.player.left > 0.5:
            self.player.left -= self.movespeed
        if self.moveright and self.player.right < GameSettings().window_width:
            self.player.right += self.movespeed
