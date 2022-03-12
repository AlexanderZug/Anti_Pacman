import pygame
from pygame.locals import *

from game_start_over_window import GameStartOverWindows
from ghost import Ghost
from game_settings import GameSettings
from ghost_enemies import Enemies
from ghost_food import Food


class AntiPacmanConfig:
    """Конфигурационный класс; создает экземпляры классов Ghost, Enemies, Food, GameStartOverWindows и GameSettings.
    В классе реализованна основная логика программы"""
    def __init__(self):
        self.window_surface = pygame.display.set_mode((GameSettings().window_width, GameSettings().window_height))
        self.main_clock = pygame.time.Clock()
        self.music_playing = True
        self.game_start_over_window = GameStartOverWindows(self.window_surface)
        self.ghost = Ghost(self.window_surface)
        self.food = Food(self.window_surface, self.ghost.player)
        self.enemies = Enemies(self.window_surface, self.ghost.player)
        self.enemies.create_enemies_dict()
        self.start_window()

    def set_pygame_events_config(self):
        """Метод обрабатывающий игровые события; включает в себя перемещение основного персонажа,
        обработку выхода из игры и game_over окно"""
        for event in pygame.event.get():
            if event.type == QUIT:
                GameSettings().terminate()
            self.ghost.move_keydown(event)
            self.music_bg_stop(event)
            self.escape_exit(event)
        self.main_clock.tick(GameSettings().FPS)
        self.game_over_window()

    def window_update(self):
        """Метод, который отрисовывает игровые события"""
        self.window_surface.fill((255, 255, 255))
        self.window_surface.blit(GameSettings().bg_img, (0, -300))
        self.ghost.move_it_speed()
        self.food.check_collisions()
        self.food.food_update()
        self.food.get_score_amount()
        self.food.get_lvl_amount()
        self.enemies.create_enemies_speed()
        self.enemies.check_collisions()
        self.enemies.get_damage()
        pygame.display.update()

    def music_bg_stop(self, event: pygame.event.Event):
        """Метод, останавливающий фоновую музыку при нажатии на клавишу m"""
        if event.type == KEYUP and event.key == K_m:
            if self.music_playing:
                pygame.mixer.music.stop()
            else:
                pygame.mixer.music.play(-1, 0.0)
            self.music_playing = not self.music_playing

    def start_window(self):
        """Методы, выводящий стартовое окно с музыкой"""
        self.game_start_over_window.start_music()
        pygame.display.update()
        self.game_start_over_window.wait_for_gamer_query_start()

    def game_over_window(self):
        """Метод, выводящий финальное окно при проигрыше и перезапускающий программу при нажатии клавиши"""
        if self.enemies.ghost_life == 0:
            pygame.mixer.music.stop()
            self.window_surface.fill(GameSettings().bg_colour)
            self.game_start_over_window.game_over_titel(self.food.score, self.food.lvl_count)
            self.game_start_over_window.game_over_photos()
            pygame.display.update()
            GameSettings.wait_for_gamer_query_final()
            self.__init__()
            self.game_start_over_window.stop_start_music()
            self.music_config_bg()

    @staticmethod
    def music_config_bg():
        """Статический метод для запуска фоновой музыки"""
        pygame.mixer.music.load('games_music/background.mp3')
        pygame.mixer.music.play(-1, 0.0)
        pygame.mixer.music.set_volume(0.06)

    @staticmethod
    def escape_exit(event):
        """Статический метод для выхода через ESC"""
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                GameSettings().terminate()
