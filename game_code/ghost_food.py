import random
import pygame
from game_settings import GameSettings
from ghost import Ghost
from ghost_enemies import Enemies


class Food:
    def __init__(self, window_surface, player):
        self.window_surface = window_surface
        self.player = player
        self.food_size = 25
        self.food_lst = []
        self.food_img = pygame.image.load('games_photos/food.png')
        self.food_img_stretched = pygame.transform.scale(self.food_img, (self.food_size, self.food_size))
        self.food_sound = pygame.mixer.Sound('games_music/food.wav')
        self.score = 0
        self.score_lvl = 0
        self.lvl_count = 1

    def create_food(self):
        for _ in range(6):
            self.food_lst.append(
                pygame.Rect(random.randint(0, GameSettings().window_width - self.food_size),
                            random.randint(0, GameSettings().window_width - self.food_size),
                            self.food_size, self.food_size))

    def check_collisions(self):
        for i in self.food_lst[:]:
            if self.player.colliderect(i):
                self.food_sound.play()
                self.score += 1
                self.score_lvl += 1
                self.food_lst.remove(i)

    def get_score_amount(self):
        score_text = GameSettings().basic_font.render(f"Score: {self.score}", False, GameSettings().text_colour)
        score_rect = score_text.get_rect()
        score_rect.bottomleft = (10, 585)
        self.window_surface.blit(score_text, score_rect)

    def get_lvl_amount(self):
        if self.score_lvl == 6:
            self.lvl_count += 1
            self.score_lvl = 0
        lvl_text = GameSettings().basic_font.render(f"Lvl.: {self.lvl_count}", False, GameSettings().text_colour)
        lvl_rect = lvl_text.get_rect()
        lvl_rect.bottomleft = (40, 565)
        self.window_surface.blit(lvl_text, lvl_rect)

    def food_update(self):
        for i in range(len(self.food_lst) + 1):
            if len(self.food_lst) + 1 != 1:
                self.window_surface.blit(self.food_img_stretched, self.food_lst[i - 1])
            else:
                Ghost.instance.speed_increase()
                Enemies.instance.speed_increase()
                self.create_food()
