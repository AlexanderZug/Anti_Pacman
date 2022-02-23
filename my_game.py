import random
import pygame
import sys
from pygame.locals import *

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
#  настройки окна
window_width = 600
window_height = 600
window_surface = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Pacman')
FPS = 60
main_clock = pygame.time.Clock()
# цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
# переменные направления
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'
MOVELEFT = MOVERIGHT = MOVEUP = MOVEDOWN = False
MOVEDSPEED = 2

# назначение шрифта
basic_font = pygame.font.SysFont('aquakana', 48)

food_size = 25
food = []
food_img = pygame.image.load('games_photos/food.png')
food_img_stretched = pygame.transform.scale(food_img, (25, 25))
for i in range(6):
    food.append(pygame.Rect(random.randint(0, window_width - food_size), random.randint(0, window_width - food_size),
                            food_size, food_size))

player = pygame.Rect(15, 360, 40, 40)
player_img = pygame.image.load('games_photos/ghost.png')
player_img_stretched = pygame.transform.scale(player_img, (40, 40))

pygame.mixer.music.load('games_music/background.mp3')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.2)
music_playing = True

enemy_sound = pygame.mixer.Sound('games_music/catch.wav')
food_sound = pygame.mixer.Sound('games_music/food.wav')
jump_sound = pygame.mixer.Sound('games_music/jump.wav')

enemy_img = pygame.image.load('games_photos/enemy.png')
commands_block_one = {'rect': pygame.Rect(250, 80, 50, 100), 'img': pygame.transform.scale(enemy_img, (60, 70)),
                      'dir': UPRIGHT}
commands_block_two = {'rect': pygame.Rect(200, 200, 20, 20), 'img': pygame.transform.scale(enemy_img, (20, 20)),
                      'dir': UPLEFT}
commands_block_three = {'rect': pygame.Rect(100, 150, 60, 60), 'img': pygame.transform.scale(enemy_img, (60, 50)),
                        'dir': DOWNLEFT}
commands_block_four = {'rect': pygame.Rect(150, 120, 30, 30), 'img': pygame.transform.scale(enemy_img, (30, 30)),
                       'dir': DOWNRIGHT}
commands_list = [commands_block_one, commands_block_two, commands_block_three, commands_block_four]

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == K_a:
                MOVERIGHT = False
                MOVELEFT = True
            if event.key == K_RIGHT or event.key == K_d:
                MOVELEFT = False
                MOVERIGHT = True
            if event.key == K_DOWN or event.key == K_s:
                MOVEUP = False
                MOVEDOWN = True
            if event.key == K_UP or event.key == K_w:
                MOVEDOWN = False
                MOVEUP = True
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == K_a:
                MOVELEFT = False
            if event.key == K_RIGHT or event.key == K_d:
                MOVERIGHT = False
            if event.key == K_DOWN or event.key == K_s:
                MOVEDOWN = False
            if event.key == K_UP or event.key == K_w:
                MOVEUP = False
            if event.key == K_SPACE:
                player.top = random.randint(0, window_height - player.height)
                player.left = random.randint(0, window_width - player.width)
                jump_sound.play()

            if event.key == K_m:
                if music_playing:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1, 0.0)
                music_playing = not music_playing

    window_surface.fill(BLACK)

    if MOVEDOWN and player.bottom < window_height:
        player.bottom += MOVEDSPEED
    if MOVEUP and player.top > 0:
        player.top -= MOVEDSPEED
    if MOVELEFT and player.left > 0.5:
        player.left -= MOVEDSPEED
    if MOVERIGHT and player.right < window_width:
        player.right += MOVEDSPEED

    for i in food[:]:
        if player.colliderect(i):
            food_sound.play()
            food.remove(i)

    for i in range(len(food) + 1):
        if len(food) + 1 != 1:
            window_surface.blit(food_img_stretched, food[i - 1])
        else:
            for i in range(6):
                food.append(pygame.Rect(random.randint(0, window_width - food_size),
                                        random.randint(0, window_width - food_size),
                                        food_size, food_size))
                MOVEDSPEED += 0.1

    for i in commands_list:
        if i['dir'] == DOWNLEFT:
            i['rect'].left -= MOVEDSPEED
            i['rect'].top += MOVEDSPEED
        if i['dir'] == DOWNRIGHT:
            i['rect'].left += MOVEDSPEED
            i['rect'].top += MOVEDSPEED
        if i['dir'] == UPLEFT:
            i['rect'].left -= MOVEDSPEED
            i['rect'].top -= MOVEDSPEED
        if i['dir'] == UPRIGHT:
            i['rect'].left += MOVEDSPEED
            i['rect'].top -= MOVEDSPEED

        if i['rect'].top < 5:
            if i['dir'] == UPLEFT:
                i['dir'] = DOWNLEFT
            if i['dir'] == UPRIGHT:
                i['dir'] = DOWNRIGHT
        if i['rect'].bottom > 595:
            if i['dir'] == DOWNLEFT:
                i['dir'] = UPLEFT
            if i['dir'] == DOWNRIGHT:
                i['dir'] = UPRIGHT
        if i['rect'].left < 5:
            if i['dir'] == DOWNLEFT:
                i['dir'] = DOWNRIGHT
            if i['dir'] == UPLEFT:
                i['dir'] = UPRIGHT
        if i['rect'].right > 595:
            if i['dir'] == DOWNRIGHT:
                i['dir'] = DOWNLEFT
            if i['dir'] == UPRIGHT:
                i['dir'] = UPLEFT
        window_surface.blit(i['img'], i['rect'])

    for i in commands_list:
        if player.colliderect(i['rect']):
            enemy_sound.play()
            text = basic_font.render('Game over', True, RED, BLACK)
            text_rect = text.get_rect()
            text_rect.centerx = window_surface.get_rect().centerx
            text_rect.centery = window_surface.get_rect().centery
            window_surface.blit(text, text_rect)
    window_surface.blit(player_img_stretched, player)

    pygame.display.update()
    main_clock.tick(FPS)
