import pygame
from pygame.locals import *

from game_settings import GameSettings


class GameStartOverWindows:
    """Класс, создающий стартвое окно и окно Game Over."""

    def __init__(self, window_surface):
        self.window_surface = window_surface
        self.speed = 3
        self.ghost_x = -250
        self.ghost_y = 530
        self.green_ghost = -100
        self.pacman_x = -410
        self.over_sound = pygame.mixer.Sound('games_music/game_over.wav')

    def titel_lbl(self):
        """Метод, создает и выводит на игровое поле название игры и
        информацию о необходимости нажатия клавиши для начала."""
        titel_text = GameSettings().start_font.render(
            "AntiPacman", True, GameSettings().start_color
        )
        titel_rect = titel_text.get_rect()
        titel_rect.center = (300, 280)
        self.window_surface.blit(titel_text, titel_rect)
        press_key_text = GameSettings().basic_font.render(
            "Press something to start", True, GameSettings().text_colour
        )
        press_key_rect = press_key_text.get_rect()
        press_key_rect.center = (300, 400)
        self.window_surface.blit(press_key_text, press_key_rect)

    def unit_move_start_window(self):
        """Метод, выводящий на стартовый экран анимацию."""
        ghost_img = pygame.image.load('games_photos/ghost.png')
        ghost_img = pygame.transform.scale(ghost_img, (40, 40))
        pacman_img = pygame.image.load('games_photos/enemy.png')
        pacman_img = pygame.transform.scale(pacman_img, (50, 50))
        green_ghost_img = pygame.image.load('games_photos/green_ghost.png')
        green_ghost_img = pygame.transform.scale(green_ghost_img, (40, 40))
        self.ghost_x += self.speed
        self.pacman_x += self.speed
        if self.ghost_x > 530:
            self.ghost_x = 530
            self.ghost_y -= self.speed
        if self.ghost_y < 520:
            self.green_ghost += self.speed
            if self.ghost_y <= -20:
                self.green_ghost -= 14
                if self.ghost_y <= -150:
                    self.ghost_x = -250
                    self.ghost_y = 530
                    self.pacman_x = -410
                    self.green_ghost = -100
        self.window_surface.blit(ghost_img, (self.ghost_x, self.ghost_y))
        self.window_surface.blit(pacman_img, (self.pacman_x, 520))
        self.window_surface.blit(green_ghost_img, (self.green_ghost, 60))
        pygame.display.update()

    def game_over_titel(self, score: int, lvl: int):
        """Метод, выводящий в случае поражения Game Over окно с печальной музыкой."""
        game_over_titel_text = GameSettings().start_font.render(
            "Game Over", True, GameSettings().start_color
        )
        game_over_titel_rect = game_over_titel_text.get_rect()
        game_over_titel_rect.center = (300, 280)
        self.window_surface.blit(game_over_titel_text, game_over_titel_rect)
        game_over_user_query = GameSettings().basic_font.render(
            "Press something to restart", True, GameSettings().text_colour
        )
        game_over_user_query_rect = game_over_user_query.get_rect()
        game_over_user_query_rect.center = (300, 500)
        self.window_surface.blit(
            game_over_user_query, game_over_user_query_rect
        )
        score_text = GameSettings().basic_font.render(
            f"Score: {score}", True, GameSettings().text_colour
        )
        score_text_rect = score_text.get_rect()
        score_text_rect.center = (200, 400)
        self.window_surface.blit(score_text, score_text_rect)
        lvl_text = GameSettings().basic_font.render(
            f"Level: {lvl}", True, GameSettings().text_colour
        )
        lvl_text_rect = lvl_text.get_rect()
        lvl_text_rect.center = (400, 400)
        self.window_surface.blit(lvl_text, lvl_text_rect)
        self.over_sound.play()

    def game_over_photos(self):
        """Метод, выводит на Game Over окно фото с расстроенными призраками."""
        end_ghosts_img = pygame.image.load('games_photos/end_photo.png')
        end_ghosts_img = pygame.transform.scale(end_ghosts_img, (150, 150))
        end_ghosts_rect = end_ghosts_img.get_rect(center=(400, 150))
        self.window_surface.blit(end_ghosts_img, end_ghosts_rect)

    def wait_for_gamer_query_start(self):
        """Метод, создающий игровой цикл и ждущий
        от игрока нажатия клавиши для старта игры;
        отрисовывает стартовые надписи и анимацию."""
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    GameSettings().terminate()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        GameSettings().terminate()
                    return
            self.window_surface.fill(GameSettings().bg_colour)
            self.titel_lbl()
            self.unit_move_start_window()

    @staticmethod
    def start_music():
        """Статичный метод для запуска стартовой музыки."""
        pygame.mixer.music.load('games_music/start_song.mp3')
        pygame.mixer.music.play(-1, 0.0)
        pygame.mixer.music.set_volume(0.09)

    @staticmethod
    def stop_start_music():
        """Статичный метод для остановки стартовой музыки.."""
        pygame.mixer.music.stop()
