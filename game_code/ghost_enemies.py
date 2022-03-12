import pygame

from game_settings import GameSettings

#
class Enemies:
    """Класс создающий врагов и подсчитывающий урон персонажа при столкновении"""
    def __init__(self, window_surface: pygame.surface.Surface, player: pygame.Rect):
        self.window_surface = window_surface
        self.player = player
        self.move_direction = ['downleft', 'downright', 'upleft', 'upright']
        self.enemy_img = pygame.image.load('games_photos/enemy.png')
        self.enemy_sound = pygame.mixer.Sound('games_music/catch.wav')
        self.enemies_lst = []
        self.move_speed = 1.5
        self.ghost_life = 50

    def speed_increase(self):
        """Метод, увеличивающий скорость врагов при переходе на новый уровень"""
        self.move_speed += 0.5

    def create_enemies_dict(self):
        """Метод, создающий словарь для каждого из врагов с экземпляром класса Rect; задает размеры врагов
        и координаты их первоначального появления"""
        commands_block_one = {'rect': pygame.Rect(250, 80, 50, 100),
                              'img': pygame.transform.scale(self.enemy_img, (60, 70)),
                              'dir': self.move_direction[3]}
        commands_block_two = {'rect': pygame.Rect(200, 200, 20, 20),
                              'img': pygame.transform.scale(self.enemy_img, (20, 20)),
                              'dir': self.move_direction[2]}
        commands_block_three = {'rect': pygame.Rect(100, 150, 60, 60),
                                'img': pygame.transform.scale(self.enemy_img, (60, 50)),
                                'dir': self.move_direction[0]}
        commands_block_four = {'rect': pygame.Rect(150, 120, 30, 30),
                               'img': pygame.transform.scale(self.enemy_img, (30, 30)),
                               'dir': self.move_direction[1]}
        self.enemies_lst = [commands_block_one, commands_block_two, commands_block_three, commands_block_four]

    def create_enemies_speed(self):
        """Метод, конфигурирующий перемещение врагов"""
        for i in self.enemies_lst:
            if i['dir'] == self.move_direction[0]:
                i['rect'].left -= self.move_speed
                i['rect'].top += self.move_speed
            if i['dir'] == self.move_direction[1]:
                i['rect'].left += self.move_speed
                i['rect'].top += self.move_speed
            if i['dir'] == self.move_direction[2]:
                i['rect'].left -= self.move_speed
                i['rect'].top -= self.move_speed
            if i['dir'] == self.move_direction[3]:
                i['rect'].left += self.move_speed
                i['rect'].top -= self.move_speed
            self.get_rebound_from_field_top_bottom(i)
            self.window_surface.blit(i['img'], i['rect'])

    def get_rebound_from_field_top_bottom(self, i: dict):
        """Метод, не позволяющий врагам выходить за границы игровой поверхности"""
        if i['rect'].top < 0:
            if i['dir'] == self.move_direction[2]:
                i['dir'] = self.move_direction[0]
            if i['dir'] == self.move_direction[3]:
                i['dir'] = self.move_direction[1]
        if i['rect'].bottom > 595:
            if i['dir'] == self.move_direction[0]:
                i['dir'] = self.move_direction[2]
            if i['dir'] == self.move_direction[1]:
                i['dir'] = self.move_direction[3]
        self.get_rebound_fromfield_legy_right(i)

    def get_rebound_fromfield_legy_right(self, i: dict):
        """Метод, не позволяющий врагам выходить за границы игровой поверхности"""
        if i['rect'].left < 5:
            if i['dir'] == self.move_direction[0]:
                i['dir'] = self.move_direction[1]
            if i['dir'] == self.move_direction[2]:
                i['dir'] = self.move_direction[3]
        if i['rect'].right > 595:
            if i['dir'] == self.move_direction[1]:
                i['dir'] = self.move_direction[0]
            if i['dir'] == self.move_direction[3]:
                i['dir'] = self.move_direction[2]

    def check_collisions(self):
        """Метод, проверяющий столкновение персонажа с врагами и уменьшающий количество его жизней"""
        for i in self.enemies_lst:
            if self.player.colliderect(i['rect']):
                self.ghost_life -= 1
                self.enemy_sound.play()

    def get_damage(self):
        """Метод, выводящий количество жизней персонажа на игровую поверхность"""
        life_text = GameSettings().basic_font.render(f"HP: {self.ghost_life}", False, GameSettings().text_colour)
        life_rect = life_text.get_rect()
        life_rect.bottomright = (565, 585)
        self.window_surface.blit(life_text, life_rect)

    def __new__(cls, *args, **kwargs):
        """Singleton"""
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
            cls.instance.__init__(*args, **kwargs)
        return cls.instance
